#SETUP BEAUTIFUL SOUP
#'import requests' lets you make http requests using python
import requests
# from (beatiful soupt v4) import package files
from bs4 import BeautifulSoup

# Setup scraped variable to access elements via the select url
# Scraped = BeautifulSoup object represents the doc as a nested data structure
url = "http://books.toscrape.com/index.html"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')



#CREATE/MAINPULATE BEATIFUL SOUP OBJECT
# Use the syntax 'scraped.element' (includes html)
print(scraped.title)
# Use strip() method combined with .text to print just the title content
print(scraped.title.text.strip())
# Alternatively you could store the title in a variable, then print it
doc_title = scraped.title.text.strip()
print(doc_title, '\n\n--------------------')

# Do this with the header tag
print(scraped.h1.text.strip())
# Do this with the title of the first book
title = scraped.article.h3.a['title']
print(title, '\n\n--------------------')

# Print all the titles from all the books (first page)
print("PRINTING ALL TITLES BELOW:\n")
all_titles = scraped.find_all("a", title=True)
for link in all_titles:
    print(link['title'])
print('\n--------------------')



# PRINT ALL PRICES FROM THE PAGE
# Use srape.select() to grab elements by CSS class selector
prices = scraped.select(".price_color")
# Print prices with a loop
for price in prices:
    print(price)
print('\n--------------------')
# Do it without the htmo formatting
for price in prices:
     price = float(price.text.lstrip('£'))
     print(price)
print('\n--------------------')
# Do it in dollars
for price in prices:
    price = float(price.text.lstrip('£'))
    price = str(price)
    print("$" + price)
print('\n--------------------')



#LAST, GRAB TITLES WITH CORRESPONDING PRICES
# Create list variable to put dictionary inside
# Grab the articles as raw html data (to manipulate in for loop below)
title_prices = []
# Use srape.select() to grab elements by CSS class selector
articles = scraped.select('.product_pod')

# Loop through, extracting the info you need using methods and bs4 syntax
for article in articles:
    title = article.h3.a['title']
    price = article.find('p', class_='price_color')
    price_float = float(price.text.lstrip('£'))
    # Append each article in articles to our dictionary (put it all together)
    title_prices.append({title: price_float}) # (create the dictinary and append to array)
#Now we can print the title_prices dictonary (that's been populated)
print(title_prices)



