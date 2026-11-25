"""Application settings, read from environment variables.

No secrets live in this file. Configure the database one of three ways:

1. DATABASE_URL - any SQLAlchemy URL (used as-is), e.g.
   mysql+pymysql://user:pass@host:3306/sandwich_maker_api
2. DB_HOST (+ DB_PORT, DB_USER, DB_PASSWORD, DB_NAME) - builds a MySQL URL.
3. Neither set - falls back to a local SQLite file (restaurant.db).

Set SEED_ON_STARTUP=true to reset the database to the demo data every time the
server starts (used by the hosted demo).
"""

import os
from urllib.parse import quote_plus


def _env_bool(name: str, default: bool = False) -> bool:
    return os.environ.get(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def _database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if url:
        return url
    host = os.environ.get("DB_HOST")
    if host:
        user = os.environ.get("DB_USER", "root")
        password = quote_plus(os.environ.get("DB_PASSWORD", ""))
        port = os.environ.get("DB_PORT", "3306")
        name = os.environ.get("DB_NAME", "sandwich_maker_api")
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}?charset=utf8mb4"
    return "sqlite:///./restaurant.db"


class conf:
    app_host = os.environ.get("APP_HOST", "0.0.0.0")
    app_port = int(os.environ.get("PORT", os.environ.get("APP_PORT", "8000")))
    database_url = _database_url()
    seed_on_startup = _env_bool("SEED_ON_STARTUP")
