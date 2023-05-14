import requests
from bs4 import BeautifulSoup

# Get the HTML of the Wegmans website.
response = requests.get("https://shop.wegmans.com/search?search_term=Eggs")

# Create a BeautifulSoup object from the HTML.
soup = BeautifulSoup(response.content, "html.parser")

# Find the price of Large Eggs.
price = soup.find("span", class_="css-zqx11d")

# Check if the price was found.
if price is not None:
    # Print the price.
    print(price.text)
else:
    print("No price found.")
