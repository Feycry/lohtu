from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    result = db.session.execute(text('SELECT id, title FROM refs'))
    references = result.fetchall()
    return [Reference(reference[0], title=reference[1]) for reference in references] 

def create_reference(author, title, booktitle, year, url=None, doi=None, editor=None, 
                     volume=None, number=None, series=None, pages=None, address=None, 
                     month=None, organization=None, publisher=None):
    sql = text('''INSERT INTO refs (author, title, booktitle, year, url, doi, editor, 
                  volume, number, series, pages, address, month, organization, publisher) 
                  VALUES (:author, :title, :booktitle, :year, :url, :doi, :editor, 
                  :volume, :number, :series, :pages, :address, :month, :organization, :publisher)''')
    db.session.execute(sql, {
        "author": author,
        "title": title,
        "booktitle": booktitle,
        "year": year,
        "url": url,
        "doi": doi,
        "editor": editor,
        "volume": volume,
        "number": number,
        "series": series,
        "pages": pages,
        "address": address,
        "month": month,
        "organization": organization,
        "publisher": publisher
    })
    db.session.commit()
