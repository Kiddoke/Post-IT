# Post-IT - Work related MVP

# Post-IT Forslagstavle

En digital forslagstavle hvor man kan opprette, flytte og slette forslag på tvers av statuser.

## Hvordan kjøre prosjektet

1. Klon repoet
```bash
git clone https://github.uio.no/kevil/Post-IT.git
cd Post-IT
```

2. Opprett og aktiver et virtuelt miljø
```bash
python -m venv env
# Windows:
env\Scripts\activate
# Mac/Linux:
source env/bin/activate
```

3. Installer avhengigheter
```bash
pip install django
```

4. Kjør migrasjoner
```bash
python manage.py migrate
```

5. Start serveren
```bash
python manage.py runserver
```

Åpne `http://127.0.0.1:8000` i nettleseren (evt. hvor enn du velger å hoste den)

## Tekniske valg

- **Django templates istedenfor React** : for en MVP av denne størrelsen er server-side rendering enklere og raskere å sette opp uten å miste funksjonalitet. Hadde altså dårlig tid
- **SQLite** : Djangos default database, tilstrekkelig og lettere for en MVP
- **Tailwind CDN** : ingen build-steg nødvendig, fungerer rett i templaten
- **Drag-and-drop med vanilla JS** : unngår eksterne biblioteker for enkel funksjonalitet

## Hva jeg ville gjort videre med mer tid

- Brukerautentisering så man kan se hvem som la inn et forslag
- Mulighet for å kommentere på forslag
- Bedre feilhåndtering (f.eks. hvis tittel eller innhold mangler)
