# Import the necessary libraries
from bs4 import BeautifulSoup
import requests

# Make an HTTP request to the webpage
response = requests.get("https://www.example.com/webpage.html")

# Parse the HTML or XML content of the webpage
soup = BeautifulSoup(response.text, "html.parser")

# Extract the desired data using Beautiful Soup's methods and attributes
data = soup.find("div", {"id": "data"})

# Print the data to the console
print(data)
