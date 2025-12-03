import os

from sqlalchemy import text

from config import app, db


def reset_db():
    print("Clearing contents from table refs")
    sql = text("DELETE FROM refs")
    db.session.execute(sql)
    db.session.commit()


def tables():
    """Returns all table names except those ending with _id_seq."""
    sql = text(
        "SELECT table_name "
        "FROM information_schema.tables "
        "WHERE table_schema = 'public' "
        "AND table_name NOT LIKE '%_id_seq'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]


def setup_db():
    """Create the database, dropping existing tables if present."""
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table} CASCADE")
            db.session.execute(sql)
        db.session.commit()



    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r", encoding="utf-8") as schema_file:
        schema_sql = schema_file.read().strip()

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()


def delete_reference(reference_id):
    """Delete a reference by its ID."""
    sql = text("DELETE FROM refs WHERE id = :reference_id")
    result = db.session.execute(sql, {"reference_id": reference_id})
    db.session.commit()
    return result.rowcount > 0


if __name__ == "__main__":
    with app.app_context():
        setup_db()
