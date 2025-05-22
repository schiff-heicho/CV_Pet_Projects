from typing import List, Optional
from flask import Flask, render_template, request
import requests
import os
import re
from dotenv import load_dotenv
from urllib.parse import quote  # Добавлено для кодирования

load_dotenv()

app = Flask(__name__)
SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")

class Recipe:
    def __init__(self, title: str, link: str, image: Optional[str] = None):
        self.title = title
        self.link = link
        self.image = image

def translate_ingredient(ingredient: str) -> str:
    translations = {
        "яблоко": "apple",
        "мука": "flour",
        "молоко": "milk",
        "яйцо": "egg",
        "сахар": "sugar",
    }
    return translations.get(ingredient.lower(), ingredient)

def parse_recipes(ingredients: List[str]) -> List[Recipe]:
    if not SPOONACULAR_API_KEY:
        return []
    
    translated_ingredients = [translate_ingredient(ingredient) for ingredient in ingredients]
    
    encoded_ingredients = quote(", ".join(translated_ingredients))
    
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "ingredients": encoded_ingredients, 
        "apiKey": SPOONACULAR_API_KEY,
        "number": 10,
        "language": "ru",
        "sort": "popularity",
        "ignorePantry": True
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"API Error: {e}")
        return []

    recipes = []
    for item in data:
        recipe_url = f"https://spoonacular.com/recipes/{item['id']}"
        recipes.append(
            Recipe(
                title=item["title"],
                link=recipe_url,
                image=item.get("image", None)
            )
        )
    return recipes

@app.route("/", methods=["GET", "POST"])
def home():
    error = None
    recipes: Optional[List[Recipe]] = None
    ingredients_str = ""

    if request.method == "POST":
        ingredients_str = request.form.get("ingredients", "")
        if not ingredients_str.strip():
            error = "Пожалуйста, введите хотя бы один ингредиент."
        else:
            raw_ingredients = ingredients_str.strip().lower()
            split_tokens = re.split(r"[,;\s]+", raw_ingredients)
            ingredients = [token.strip() for token in split_tokens if token]

            if not ingredients:
                error = "Не удалось распарсить ингредиенты. Пожалуйста, введите корректные данные."
            else:
                recipes = parse_recipes(ingredients)
                if not recipes:
                    error = "К сожалению, рецепты с такими ингредиентами не найдены."

    return render_template(
        "index.html",
        recipes=recipes,
        error=error,
        ingredients=ingredients_str,
    )

if __name__ == "__main__":
    app.run(debug=True)
