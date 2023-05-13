import json
import random

# Load meal options with corresponding ingredients and recipes
with open("meals.json", "r") as f:
    meals = json.load(f)

breakfast_options = list(meals.keys())[:2]
lunch_options = list(meals.keys())[2:4]
dinner_options = list(meals.keys())[4:]

# Define meal plan
meal_plan = {}
for day in [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]:
    meal_plan[day] = {"breakfast": random.choice(breakfast_options)}
    meal_plan[day]["lunch"] = random.choice(lunch_options)
    meal_plan[day]["dinner"] = random.choice(dinner_options)

# Define shopping list
shopping_list = {}
for day in meal_plan:
    for meal in meal_plan[day]:
        for ingredient in meals[meal_plan[day][meal]]["ingredients"]:
            if ingredient not in shopping_list:
                shopping_list[ingredient] = 1
            else:
                shopping_list[ingredient] += 1

html = "<html><body>" + "<h1>Meal Plan:</h1>"
for day in meal_plan:
    html += f"<h2>{day}</h2>"
    for meal_time in ["breakfast", "lunch", "dinner"]:
        meal = meal_plan[day][meal_time]
        html += f"<p><strong>{meal_time.capitalize()}:</strong> {meal}</p>"
        html += f'<p><strong>Recipe:</strong> {meals[meal]["recipe"]}</p>'
    html += "<br>"

html += "<h1>Shopping List:</h1>"
for ingredient in shopping_list:
    html += f"<p>{ingredient} - {shopping_list[ingredient]}</p>"
html += "</body></html>"

# Write HTML to file
with open("meal_plan.html", "w") as f:
    f.write(html)
