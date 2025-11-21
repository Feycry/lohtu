class Reference:
    # Currently only id is required, this might need to change in the future
    def __init__(self, id, ref_type=None, author=None, title=None, booktitle=None, year=None, 
                 editor=None, volume=None, number=None, series=None, pages=None,
                 address=None, month=None, organization=None, publisher=None, 
                 url=None, doi=None, edition=None, howpublished=None, 
                 institution=None, journal=None, note=None, school=None, type=None):
        self.id = id
        self.ref_type = ref_type
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
        self.edition = edition
        self.howpublished = howpublished
        self.institution = institution
        self.journal = journal
        self.note = note
        self.school = school
        self.type = type

    def __str__(self):
        parts = []
        if self.ref_type:
            parts.append(f"Type: @{self.ref_type}")
        if self.author:
            parts.append(f"Author: {self.author}")
        if self.title:
            parts.append(f"Title: {self.title}")
        if self.journal:
            parts.append(f"Journal: {self.journal}")
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
        if self.edition:
            parts.append(f"Edition: {self.edition}")
        if self.howpublished:
            parts.append(f"How published: {self.howpublished}")
        if self.institution:
            parts.append(f"Institution: {self.institution}")
        if self.school:
            parts.append(f"School: {self.school}")
        if self.note:
            parts.append(f"Note: {self.note}")
        if self.type:
            parts.append(f"Type: {self.type}")
        if self.url:
            parts.append(f"URL: {self.url}")
        if self.doi:
            parts.append(f"DOI: {self.doi}")
        return ", ".join(parts) if parts else f"Reference #{self.id}"
