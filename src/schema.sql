CREATE TABLE refs (
    id SERIAL PRIMARY KEY,
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
    publisher TEXT
);

CREATE TABLE refType (
    id SERIAL PRIMARY KEY
);