import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/Subhas_Chandra_Bose'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Extract all text content from the webpage
text_content = soup.get_text()

# Print or do whatever you want with the extracted text
print(text_content)
