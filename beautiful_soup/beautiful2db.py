from bs4 import BeautifulSoup
import urllib.request
import sqlite3
from datetime import datetime


# conn = sqlite3.connect('beautiful_soup/example2.db')
conn = sqlite3.connect('example2.db')
c = conn.cursor()
# c.execute('''drop table bloom''')
c.execute('''CREATE TABLE IF NOT EXISTS bloom
             (date text, name text, price real)''')

# Save (commit) the changes
conn.commit()

url = ['http://207.246.85.12/nasdaq.html', 'http://207.246.85.12/500.html']
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
    stockers = ([name, price])
    # stockers = ([name, price, datetime.now()])
    print(stockers)
    bugger = len([name, price])
    print(bugger)

    # Now lets insert some data
    ins = conn.cursor()
    ins.execute('INSERT INTO bloom(name, price, date) VALUES(?,?,?)',
                [name, price, datetime.now()])
    id = ins.lastrowid
    print('Last row id: %d' % id)
    conn.commit()

for row in c.execute('SELECT * FROM bloom ORDER BY date'):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
