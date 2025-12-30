from sqlalchemy import String, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from .db import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # e.g. "Garlic Prawn Pasta"
    name: Mapped[str] = mapped_column(String(200), nullable=False)

    # "seafood" or "meat"
    category: Mapped[str] = mapped_column(String(20), nullable=False)

    # comma-separated tags for quick prototype:
    # e.g. "daily", "festival:christmas", "special:wedding", "exclude:beef"
    tags: Mapped[str] = mapped_column(String(500), nullable=False, default="")

    # base servings for ingredient scaling
    base_servings: Mapped[int] = mapped_column(Integer, nullable=False, default=2)

    # Ingredients in simple text lines
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)

    # Steps in simple text lines
    steps: Mapped[str] = mapped_column(Text, nullable=False)
