from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    result = db.session.execute(text('SELECT id, title FROM refs'))
    references = result.fetchall()
    return [Reference(reference[0], title=reference[1]) for reference in references] 

def create_reference(content):
    sql = text('INSERT INTO refs (content) VALUES (:content)')
    db.session.execute(sql, { "content": content })
    db.session.commit()
