To run:

    export FLASK_APP=app.py
    flask run

Exposes a single endpoint: `host/?q=...`

When a query string is passed, magical ML transforms it into the top 10
highest rated matching strains