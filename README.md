# lohtu
Ohjelmistotuotantotokurssin projekti

# Definition of Done
- Unit tests are written and passing
- There are no known bugs
- Code is in English and follows agreed coding standards

# Backlog
https://docs.google.com/spreadsheets/d/1CTdGofwCAQt9wFUSohZNbdltgjcS-296MohrMO4q4kg/edit?gid=1#gid=1

# Start manual
1. Install dependencies
   poetry install
2. Create .env file and copy the text below. Replace secret key
   DATABASE_URL=postgresql://...
   TEST_ENV=true
   SECRET_KEY=...
3. Activate the virtual environment
   eval $(poetry env activate)
4. Start the application
   python3 src/index.py
