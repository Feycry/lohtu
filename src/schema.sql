CREATE TABLE refType (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    required_fields TEXT[] NOT NULL
);

CREATE TABLE refs (
    id SERIAL PRIMARY KEY,
    ref_type_id INTEGER REFERENCES refType(id),
    author TEXT,
    title TEXT,
    booktitle TEXT,
    year TEXT,
    url TEXT,
    doi TEXT,
    editor TEXT,
    volume TEXT,
    number TEXT,
    series TEXT,
    pages TEXT,
    address TEXT,
    month TEXT,
    organization TEXT,
    publisher TEXT,
    edition TEXT,
    howpublished TEXT,
    institution TEXT,
    journal TEXT,
    note TEXT,
    school TEXT,
    type TEXT
);

INSERT INTO refType (name, required_fields) VALUES 
    ('article', ARRAY['author', 'title', 'journal', 'year']),
    ('book', ARRAY['author', 'title', 'publisher', 'year']),
    ('booklet', ARRAY['title']),
    ('conference', ARRAY['author', 'title', 'booktitle', 'year']),
    ('inbook', ARRAY['author', 'title', 'booktitle', 'publisher', 'year']),
    ('incollection', ARRAY['author', 'title', 'booktitle', 'publisher', 'year']),
    ('inproceedings', ARRAY['author', 'title', 'booktitle', 'year']),
    ('manual', ARRAY['title']),
    ('mastersthesis', ARRAY['author', 'title', 'school', 'year']),
    ('misc', ARRAY[]::TEXT[]),
    ('phdthesis', ARRAY['author', 'title', 'school', 'year']),
    ('proceedings', ARRAY['title', 'year']),
    ('techreport', ARRAY['author', 'title', 'institution', 'year']),
    ('unpublished', ARRAY['author', 'title']);