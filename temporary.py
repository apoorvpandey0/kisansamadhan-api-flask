import requests
from bs4 import BeautifulSoup

url = 'https://www.learncbse.in/ncert-solutions-for-class-9-maths-number-system/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
results = soup.find_all('div', class_='entry-content')
print(results[0].encode("utf-8"))
