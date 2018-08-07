from bs4 import BeautifulSoup
import urllib.request
import csv
from datetime import datetime


url = ['https://www.bloomberg.com/quote/CCMP:IND', 'https://www.bloomberg.com/quote/SPX:IND']
data = []
for pg in url:
    # page = urllib.request.urlopen(pg)
    page = urllib.request.urlopen(pg)

    # urllib2 is python 2 only
    # Finally, parse the page into BeautifulSoup format so we can use
    # BeautifulSoup to work on it.

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # Take out the <div> of name and get its value
    name_box = soup.find('h1', attrs={'class': 'name'})

    # After we have the tag, we can get the data by getting its text.

    # strip() is used to remove starting and trailing
    name = name_box.text.strip()

    print(name)

    # Similarly, we can get the price too.

    price_box = soup.find('div', attrs={'class': 'price'})
    price = price_box.text
    print(price)

# Prints out the current price of the S&P 500 Index.


# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    # The for loop
    for name, price in data:
        writer.writerow([name, price, datetime.now()])
