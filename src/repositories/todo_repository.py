from config import db
from sqlalchemy import text

from entities.todo import Todo

def get_todos():
    result = db.session.execute(text("SELECT id, content, done FROM todos"))
    todos = result.fetchall()
    return [Todo(todo[0], todo[1], todo[2]) for todo in todos] 

def set_done(todo_id):
    sql = text("UPDATE todos SET done = TRUE WHERE id = :id")
    db.session.execute(sql, { "id": todo_id })
    db.session.commit()

def create_todo(content):
    sql = text("INSERT INTO todos (content) VALUES (:content)")
    db.session.execute(sql, { "content": content })
    db.session.commit()
