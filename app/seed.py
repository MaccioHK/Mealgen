from sqlalchemy.orm import Session
from .models import Recipe

def seed_if_empty(db: Session) -> None:
    if db.query(Recipe).count() > 0:
        return

    samples = [
        Recipe(
            name="Garlic Prawn Pasta",
            category="seafood",
            tags="daily",
            base_servings=2,
            ingredients="\n".join([
                "200 g prawns",
                "180 g spaghetti",
                "2 tbsp olive oil",
                "2 cloves garlic (minced)",
                "100 g cherry tomatoes",
                "1 tbsp lemon juice",
                "Salt and black pepper",
            ]),
            steps="\n".join([
                "Cook the spaghetti until al dente.",
                "Sauté garlic in olive oil for 30 seconds.",
                "Add prawns and cook until pink.",
                "Add tomatoes and lemon juice, season well.",
                "Toss with pasta and serve.",
            ]),
        ),
        Recipe(
            name="Salmon with Herb Butter",
            category="seafood",
            tags="festival:easter",
            base_servings=2,
            ingredients="\n".join([
                "2 salmon fillets",
                "1 tbsp butter",
                "1 tbsp chopped parsley",
                "1 tsp lemon zest",
                "Salt and black pepper",
            ]),
            steps="\n".join([
                "Season salmon and pan-fry skin-side down until crisp.",
                "Flip briefly to finish cooking.",
                "Mix butter with parsley and lemon zest.",
                "Top salmon with herb butter and serve.",
            ]),
        ),
        Recipe(
            name="Roast Turkey with Gravy",
            category="meat",
            tags="festival:christmas,exclude:pork,exclude:lamb,exclude:beef",
            base_servings=4,
            ingredients="\n".join([
                "1.6 kg turkey breast joint",
                "2 tbsp olive oil",
                "1 tsp salt",
                "1 tsp black pepper",
                "500 ml chicken stock",
                "1 tbsp flour",
            ]),
            steps="\n".join([
                "Rub turkey with oil, salt and pepper.",
                "Roast until cooked through (check juices run clear).",
                "Rest meat, then make gravy with stock and flour.",
                "Slice and serve with gravy.",
            ]),
        ),
        Recipe(
            name="Beef Stir-fry with Veg",
            category="meat",
            tags="daily,exclude:beef",
            base_servings=2,
            ingredients="\n".join([
                "250 g beef strips",
                "1 tbsp soy sauce",
                "1 tbsp oil",
                "1 bell pepper (sliced)",
                "1 onion (sliced)",
            ]),
            steps="\n".join([
                "Heat oil in a wok/pan.",
                "Stir-fry beef quickly, then add veg.",
                "Add soy sauce and toss until coated.",
                "Serve hot.",
            ]),
        ),
        Recipe(
            name="Pork Belly Celebration Bites",
            category="meat",
            tags="special:wedding,exclude:pork",
            base_servings=4,
            ingredients="\n".join([
                "600 g pork belly",
                "1 tbsp honey",
                "1 tbsp soy sauce",
                "1 tsp five-spice",
            ]),
            steps="\n".join([
                "Roast pork belly until crisp.",
                "Brush with honey/soy glaze near the end.",
                "Slice into bite-size pieces and sprinkle five-spice.",
            ]),
        ),
        Recipe(
            name="Lamb Chops for Two",
            category="meat",
            tags="special:anniversary,exclude:lamb",
            base_servings=2,
            ingredients="\n".join([
                "2 lamb chops",
                "1 tbsp olive oil",
                "1 tsp rosemary",
                "Salt and black pepper",
            ]),
            steps="\n".join([
                "Season chops with rosemary, salt and pepper.",
                "Pan-fry to your preferred doneness.",
                "Rest for 3 minutes then serve.",
            ]),
        ),
        Recipe(
            name="Seafood Platter (Friends Night)",
            category="seafood",
            tags="special:friends",
            base_servings=4,
            ingredients="\n".join([
                "400 g mixed seafood (prawns, squid, mussels)",
                "2 tbsp olive oil",
                "2 cloves garlic (minced)",
                "1 lemon (wedges)",
                "Salt and black pepper",
            ]),
            steps="\n".join([
                "Heat oil and sauté garlic briefly.",
                "Cook seafood until just done.",
                "Season and serve with lemon wedges.",
            ]),
        ),
    ]

    db.add_all(samples)
    db.commit()
