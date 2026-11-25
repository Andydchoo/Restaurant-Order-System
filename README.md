# Restaurant Order System

A restaurant ordering app with a FastAPI + SQLAlchemy backend and a plain HTML/CSS/JS frontend. Customers can browse the menu, apply promo codes, place orders and review dishes. Staff can manage menu items, promotions and orders.

**Live demo:** _add your Render URL here_ (free hosting, so the first load after the app has been idle can take about a minute)

| Account | Email | Password |
|---|---|---|
| Customer | `alice.johnson@email.com` | `password123` |
| Staff | `staff@restaurant.com` | `staffpass123` |

The hosted demo resets to this sample data whenever the server restarts. Interactive API docs are at `/docs`.

Built as the ITSC 3155 final project by Nate Gustafson, Andy Choo, Jeevan Liu, Caimen French and Andy Nguyen. Original team repository: [illcommittee/ITSC3155-FinalProject](https://github.com/illcommittee/ITSC3155-FinalProject).

## Run locally

```bash
pip install -r requirements.txt
SEED_ON_STARTUP=true uvicorn api.main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) for the app and [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the API docs. Without any database settings the app uses a local SQLite file, `restaurant.db`. Leave out `SEED_ON_STARTUP` to keep your data between restarts, or run `python seed.py` to reset it.

### Use MySQL instead

Set either `DATABASE_URL` (any SQLAlchemy URL, e.g. `mysql+pymysql://user:pass@localhost:3306/restaurant`) or `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD` and `DB_NAME`. See `api/dependencies/config.py`.

### Run the tests

```bash
pytest
```

## Deploy

`render.yaml` defines a free Render web service. In Render, choose **New > Blueprint**, connect this repository and deploy. It installs `requirements.txt`, starts `uvicorn api.main:app` and seeds the demo data on every boot.
