#import requests
import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()
html = scraper.get("https://www.stadiumgoods.com/en-us/")
soup = BeautifulSoup(html.text, features='html.parser')
#print(soup)

prices = []

shoe_price = soup.find("data-test"=="product-salePrice").text
prices.append(shoe_price)

print(prices)
#results = soup.find('data-test'=="productThumbnail-productName")

#URL = "https://www.stadiumgoods.com/en-us/"
#page = requests.get(URL)

#soup = BeautifulSoup(page.content, 'html.parser')

#print(results)