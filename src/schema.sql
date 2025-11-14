CREATE TABLE todos (
  id SERIAL PRIMARY KEY, 
  content TEXT NOT NULL,
  done BOOLEAN DEFAULT FALSE
)

CREATE TABLE sources (
    id SERIAL PRIMARY KEY,
    author TEXT,
    title TEXT,
    booktitle TEXT,
    year INT,
    editor TEXT,
    volume INT,
    number INT,
    series TEXT,
    pages TEXT,
    address TEXT,
    month TEXT,
    organization TEXT,
    publisher TEXT,
    url TEXT,
    doi TEXT
);

CREATE TABLE sourceType (
    id SERIAL PRIMARY KEY
);