import json
import requests
from bs4 import BeautifulSoup


# Load meal options with corresponding ingredients and recipes
with open("meals.json", "r") as f:
    meals = json.load(f)

# Get prices for each ingredient in each meal


def get_price(ingredient):
    url = (
        f"https://www.website.com/search?query={ingredient}"  # Replace with actual URL
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("span", {"class": "price"}).text  # Update with actual HTML tags
    return price


for meal in meals:
    for ingredient in meals[meal]["ingredients"]:
        price = get_price(ingredient)
        # Add the price to the meals dictionary
        meals[meal][ingredient] = price

# Save the updated meals dictionary back to the JSON file
with open("meals.json", "w") as f:
    json.dump(meals, f, indent=4)
