import random
from typing import Optional
from .schemas import GenerateRequest
from .models import Recipe
from .repository import RecipeRepository

def _parse_tags(tags_str: str) -> set[str]:
    return {t.strip().lower() for t in tags_str.split(",") if t.strip()}

def _matches(req: GenerateRequest, recipe: Recipe) -> bool:
    tags = _parse_tags(recipe.tags)

    # meal type matching
    if req.meal_type == "daily":
        if "daily" not in tags:
            return False

    elif req.meal_type == "special":
        if req.special_kind is None:
            return False
        if f"special:{req.special_kind.lower()}" not in tags:
            return False

    elif req.meal_type == "festival":
        if req.festival_kind is None:
            return False
        if f"festival:{req.festival_kind.lower()}" not in tags:
            return False
    else:
        return False

    # exclusions: if user excludes beef, recipe must NOT contain exclude:beef
    for ex in req.exclusions:
        if f"exclude:{ex.lower()}" in tags:
            return False

    return True

def scale_ingredients(ingredients_text: str, base_servings: int, target_servings: int) -> str:
    """
    Simple scaling: assumes lines like "200 g prawns" or "2 tbsp olive oil"
    We only scale leading numeric values (int/float) for prototype.
    """
    import re

    factor = target_servings / max(base_servings, 1)

    def scale_line(line: str) -> str:
        m = re.match(r"^\s*(\d+(\.\d+)?)\s+(.*)$", line)
        if not m:
            return line
        qty = float(m.group(1))
        rest = m.group(3)
        new_qty = qty * factor
        # format nicely
        if abs(new_qty - round(new_qty)) < 1e-9:
            qty_str = str(int(round(new_qty)))
        else:
            qty_str = f"{new_qty:.1f}".rstrip("0").rstrip(".")
        return f"{qty_str} {rest}"

    lines = [scale_line(l) for l in ingredients_text.splitlines()]
    return "\n".join(lines)

class MealGeneratorService:
    def __init__(self, repo: RecipeRepository):
        self.repo = repo

    def generate(self, req: GenerateRequest) -> Optional[dict]:
        recipes = self.repo.list_by_category(req.category)
        candidates = [r for r in recipes if _matches(req, r)]

        if not candidates:
            return None

        chosen = random.choice(candidates)

        scaled_ingredients = scale_ingredients(
            ingredients_text=chosen.ingredients,
            base_servings=chosen.base_servings,
            target_servings=req.persons
        )

        return {
            "name": chosen.name,
            "category": chosen.category,
            "persons": req.persons,
            "meal_type": req.meal_type,
            "special_kind": req.special_kind,
            "festival_kind": req.festival_kind,
            "ingredients": scaled_ingredients,
            "steps": chosen.steps,
        }
