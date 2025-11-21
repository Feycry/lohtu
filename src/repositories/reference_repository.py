from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_reference_type_required_fields(reference_type):
    """Get the required fields for a specific reference type."""
    sql = text('SELECT required_fields FROM refType WHERE name = :reference_type')
    result = db.session.execute(sql, {"reference_type": reference_type})
    row = result.fetchone()
    return row[0] if row else []

def get_references():
    result = db.session.execute(text('''SELECT id, author, title, booktitle, year, url, doi, 
                                        editor, volume, number, series, pages, address, 
                                        month, organization, publisher FROM refs'''))
    references = result.fetchall()
    return [Reference(
        reference[0],
        author=reference[1],
        title=reference[2],
        booktitle=reference[3],
        year=reference[4],
        url=reference[5],
        doi=reference[6],
        editor=reference[7],
        volume=reference[8],
        number=reference[9],
        series=reference[10],
        pages=reference[11],
        address=reference[12],
        month=reference[13],
        organization=reference[14],
        publisher=reference[15]
    ) for reference in references] 

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
