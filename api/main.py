from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from .routers import index as router_index
from .models import model_loader
from .dependencies.config import conf


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_loader.index()

if conf.seed_on_startup:
    # Hosted demo: reset to known demo data on every boot.
    from seed import seed_database
    seed_database()

router_index.load_routes(app)

# Serve the frontend pages from the same server so the demo is one URL.
# Each folder keeps its own path because the pages link to each other with
# relative paths like ../menu_template/menu.html.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIRS = ["menu_template", "login_template", "orders_template", "staff_template", "group_bio_template"]

for folder in FRONTEND_DIRS:
    app.mount(f"/{folder}", StaticFiles(directory=PROJECT_ROOT / folder, html=True), name=folder)


@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/menu_template/menu.html")


if __name__ == "__main__":
    uvicorn.run(app, host=conf.app_host, port=conf.app_port)
