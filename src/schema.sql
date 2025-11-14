CREATE TABLE refs (
    id SERIAL PRIMARY KEY,
    author TEXT,
    title TEXT,
    booktitle TEXT,
    year INT,
    url TEXT,
    doi TEXT,
    editor TEXT,
    volume INT,
    number INT,
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