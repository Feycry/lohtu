[![codecov](https://codecov.io/gh/Feycry/lohtu/graph/badge.svg?token=B4YSGFHEO1)](https://codecov.io/gh/Feycry/lohtu)
[![GHA workflow badge](https://github.com/Feycry/lohtu/blob/main/.github/workflows/main.yml)

# lohtu
Ohjelmistotuotantotokurssin projekti

# Definition of Done
- Unit tests are written and passing
- There are no known bugs
- Code is in English and follows agreed coding standards

# Backlog
https://docs.google.com/spreadsheets/d/1CTdGofwCAQt9wFUSohZNbdltgjcS-296MohrMO4q4kg/edit?usp=sharing

# Start manual
1. Install dependencies<br>
   poetry install
2. Create .env file and copy the text below. Replace secret key<br>
   DATABASE_URL=postgresql://...<br>
   TEST_ENV=true<br>
   SECRET_KEY=...<br>
3. Activate the virtual environment<br>
   eval $(poetry env activate)<br>
4. Start the application<br>
   python3 src/index.py<br>

# Lisenssi
Mozilla Public-lisenssi 2.0
