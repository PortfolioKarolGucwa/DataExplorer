# DataExplorer

A small Django app for uploading CSV files and getting a quick look at what's in them — a preview of the rows, column types, missing-value counts, and basic descriptive statistics for any numeric columns. I built it to practice tying Django together with pandas (and a bit of matplotlib) on an actual, working feature instead of a tutorial project.

## What it does

- Upload a CSV (with a title), stored and listed on the home page
- Open a dataset to see:
  - row/column counts and per-column type + missing-value info
  - a bar chart of missing values per column
  - `describe()`-style stats (count, mean, std, min/max, quartiles) for numeric columns
  - a preview of the first 10 rows
- Delete a dataset (removes both the DB record and the uploaded file)
- Basic validation on upload — only `.csv`, capped at 5 MB

## Tech stack

Django 6, pandas for reading/summarizing the CSV, matplotlib for the chart, SQLite as the database, Bootstrap for styling (via CDN, no build step). No JS framework, no auth, no background task queue — kept deliberately simple.

## Running it locally

```bash
git clone <this-repo-url>
cd DataExplorer

python -m venv venv
venv\Scripts\activate      # on Windows
# source venv/bin/activate # on macOS/Linux

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Then open `http://127.0.0.1:8000/`.

By default `DEBUG` is on and a development `SECRET_KEY` is baked in, which is fine for running this locally but not for deploying it anywhere public. Both can be overridden with the `DEBUG` and `SECRET_KEY` environment variables.

## Project layout

Two apps, split by responsibility:

- `datasets/` — the upload form, the `UploadedFile` model, and the list/delete views. Owns the files.
- `analysis/` — reads a CSV with pandas and builds the summary (stats, chart, preview). Doesn't own any data of its own, just reads what `datasets` stores.

## Running the tests

```bash
python manage.py test
```

## Things I'd add next

- Pagination on the dataset list once there are more than a handful of files
- Handling bigger CSVs without loading the whole thing into memory
- A proper production setup (Postgres, static file storage, `django-environ` or similar for config) if this ever needed to go beyond local/demo use
- More chart options — right now it's just the one, missing-values-per-column bar chart
