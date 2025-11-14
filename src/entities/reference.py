class Reference:
    def __init__(self, id, author=None, title=None, booktitle=None, year=None, 
                 editor=None, volume=None, number=None, series=None, pages=None,
                 address=None, month=None, organization=None, publisher=None, 
                 url=None, doi=None):
        self.id = id
        self.author = author
        self.title = title
        self.booktitle = booktitle
        self.year = year
        self.editor = editor
        self.volume = volume
        self.number = number
        self.series = series
        self.pages = pages
        self.address = address
        self.month = month
        self.organization = organization
        self.publisher = publisher
        self.url = url
        self.doi = doi

    def __str__(self):
        parts = []
        if self.author:
            parts.append(f"Author: {self.author}")
        if self.title:
            parts.append(f"Title: {self.title}")
        if self.year:
            parts.append(f"Year: {self.year}")
        return ", ".join(parts) if parts else f"Reference #{self.id}"
