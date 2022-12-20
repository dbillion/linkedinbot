import requests
from bs4 import BeautifulSoup

url = "https://subslikescript.com/movies"

# Make a request to the given url
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element with tag “ul” and class “scripts-list”
ul = soup.find('ul', class_='scripts-list')

# Find all the “a” elements inside
a_tags = ul.find_all('a')

# Print the text attribute
for a in a_tags:
    print(a.text)