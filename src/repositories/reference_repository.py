from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    result = db.session.execute(text("SELECT id, content, done FROM references"))
    references = result.fetchall()
    return [Reference(reference[0], reference[1], reference[2]) for reference in references] 

def set_done(reference_id):
    sql = text("UPDATE references SET done = TRUE WHERE id = :id")
    db.session.execute(sql, { "id": reference_id })
    db.session.commit()

def create_reference(content):
    sql = text("INSERT INTO references (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()
