from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from .db import engine, SessionLocal, Base
from .seed import seed_if_empty
from .repository import RecipeRepository
from .services import MealGeneratorService
from .schemas import GenerateRequest

app = FastAPI(title="Meal Generator Prototype")

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_seed():
    db = SessionLocal()
    try:
        seed_if_empty(db)
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    category: str = Form(...),                 # "seafood" | "meat"
    persons: int = Form(...),
    meal_type: str = Form(...),                # "daily" | "special" | "festival"
    exclusions: list[str] = Form(default=[]),  # checkbox list
    special_kind: str | None = Form(default=None),
    festival_kind: str | None = Form(default=None),
):
    db = SessionLocal()
    try:
        repo = RecipeRepository(db)
        service = MealGeneratorService(repo)

        req = GenerateRequest(
            category=category,
            exclusions=exclusions,
            persons=max(1, min(persons, 12)),   # simple guard
            meal_type=meal_type,
            special_kind=special_kind,
            festival_kind=festival_kind,
        )

        result = service.generate(req)
        return templates.TemplateResponse(
            "result.html",
            {"request": request, "result": result, "req": req},
        )
    finally:
        db.close()

