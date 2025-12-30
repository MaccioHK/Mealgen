from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Recipe

class RecipeRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_by_category(self, category: str) -> list[Recipe]:
        stmt = select(Recipe).where(Recipe.category == category)
        return list(self.db.execute(stmt).scalars().all())
