class Reference:
    # Currently only id is required, this might need to change in the future
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
        if self.booktitle:
            parts.append(f"Booktitle: {self.booktitle}")
        if self.year:
            parts.append(f"Year: {self.year}")
        if self.editor:
            parts.append(f"Editor: {self.editor}")
        if self.volume:
            parts.append(f"Volume: {self.volume}")
        if self.number:
            parts.append(f"Number: {self.number}")
        if self.series:
            parts.append(f"Series: {self.series}")
        if self.pages:
            parts.append(f"Pages: {self.pages}")
        if self.address:
            parts.append(f"Address: {self.address}")
        if self.month:
            parts.append(f"Month: {self.month}")
        if self.organization:
            parts.append(f"Organization: {self.organization}")
        if self.publisher:
            parts.append(f"Publisher: {self.publisher}")
        if self.url:
            parts.append(f"URL: {self.url}")
        if self.doi:
            parts.append(f"DOI: {self.doi}")
        return ", ".join(parts) if parts else f"Reference #{self.id}"
