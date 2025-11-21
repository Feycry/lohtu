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
    result = db.session.execute(text('''SELECT r.id, rt.name, r.author, r.title, r.booktitle, r.year, r.url, r.doi, 
                                        r.editor, r.volume, r.number, r.series, r.pages, r.address, 
                                        r.month, r.organization, r.publisher, r.edition, r.howpublished,
                                        r.institution, r.journal, r.note, r.school, r.type 
                                        FROM refs r 
                                        LEFT JOIN refType rt ON r.ref_type_id = rt.id'''))
    references = result.fetchall()
    return [Reference(
        reference[0],
        ref_type=reference[1],
        author=reference[2],
        title=reference[3],
        booktitle=reference[4],
        year=reference[5],
        url=reference[6],
        doi=reference[7],
        editor=reference[8],
        volume=reference[9],
        number=reference[10],
        series=reference[11],
        pages=reference[12],
        address=reference[13],
        month=reference[14],
        organization=reference[15],
        publisher=reference[16],
        edition=reference[17],
        howpublished=reference[18],
        institution=reference[19],
        journal=reference[20],
        note=reference[21],
        school=reference[22],
        type=reference[23]
    ) for reference in references] 

def get_reference_type_id(reference_type):
    """Get the ID for a specific reference type."""
    sql = text('SELECT id FROM refType WHERE name = :reference_type')
    result = db.session.execute(sql, {"reference_type": reference_type})
    row = result.fetchone()
    return row[0] if row else None

def create_reference(reference_type, author=None, title=None, booktitle=None, year=None, 
                     url=None, doi=None, editor=None, volume=None, number=None, 
                     series=None, pages=None, address=None, month=None, 
                     organization=None, publisher=None, edition=None, 
                     howpublished=None, institution=None, journal=None, 
                     note=None, school=None, type=None):
    ref_type_id = get_reference_type_id(reference_type)
    sql = text('''INSERT INTO refs (ref_type_id, author, title, booktitle, year, url, doi, editor, 
                  volume, number, series, pages, address, month, organization, publisher,
                  edition, howpublished, institution, journal, note, school, type) 
                  VALUES (:ref_type_id, :author, :title, :booktitle, :year, :url, :doi, :editor, 
                  :volume, :number, :series, :pages, :address, :month, :organization, :publisher,
                  :edition, :howpublished, :institution, :journal, :note, :school, :type)''')
    db.session.execute(sql, {
        "ref_type_id": ref_type_id,
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
        "publisher": publisher,
        "edition": edition,
        "howpublished": howpublished,
        "institution": institution,
        "journal": journal,
        "note": note,
        "school": school,
        "type": type
    })
    db.session.commit()
