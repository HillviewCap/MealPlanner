import json
import requests

# Get the meals from the JSON file.
with open("meals.json") as f:
    meals = json.load(f)

# Create a list of ingredients for each meal.
ingredients = []
for meal in meals:
    ingredients.append(meal["ingredients"])

# Get the price of each ingredient from Wegmans.
prices = []
for ingredients in ingredients:
    for ingredient in ingredients:
        response = requests.get(f"https://www.wegmans.com/api/products/search?query={ingredient}")
        if response.status_code == 200:
            price = response.json()[0]["salePrice"]
            prices.append(price)

# Print the price of each meal.
for meal, price in zip(meals, prices):
    print(f"{meal['name']}: ${price}")
