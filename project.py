from bs4 import BeautifulSoup
import requests
from pprint import pprint

current_link = 'https://books.toscrape.com/index.html'
product_page_url = requests.get(current_link).text
soup  = BeautifulSoup(product_page_url, 'html.parser')
links = soup.find_all('div',class_='image_container')
url = 'https://books.toscrape.com/'
categories = set()
pages = [url]

for i in range(2,51):
    path = 'catalougue/page-' + str(i) + '.html'
    pages.append(url + path)
# functions to get information
books = []

def get_info(soup):

    table = soup.select('.product_page .table.table-striped')[0]
    table_body = table.find('tbody')
    title = soup.select('.col-sm-6.product_main')[0].find('h1').text
    upc_code = ''
    price_excluding_tax = ''
    price_including_tax = ''
    number_available_element = soup.select('.instock.availability')[0]
    number_available = ''.join(filter(str.isdigit, str(number_available_element)))
    product_description = soup.select('#product_description + p')[0].text
    category = soup.select('.breadcrumb')[0].find_all('a')[2].text
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.select('.product_page .item.active')[0].find('img').attrs['src']

    for row in table.find_all('tr'):
      if row.find('th').text.upper() == 'UPC':
          upc_code = row.find('td').text
      elif row.find('th').text.upper() == 'PRICE (EXCL. TAX)':
          price_excl_tax = row.find('td').text.replace('Â','').replace('£', '')
      elif row.find('th').text.upper() == 'PRICE (INCL. TAX)':
          price_incl_tax = row.find('td').text.replace('Â','').replace('£', '')


    book = {'title' : title,
                  'Available Books' : number_available,
                  'UPC Code' : upc_code,
                  'Price Excluding Tax' : price_excl_tax,
                  'Price Including Tax' : price_incl_tax,
                  'Product Description' : product_description,
                  'Category' : category,
                  'Review Rating' : review_rating,
                  'Image URL' : image_url,
                 'Product Page URL' : current_link}
    categories.add(book['Category'])

    return book


for i in pages:
    # product_page_url = requests.get(i).text;
    current_link = i
    for book in links:
        current_link = 'https://books.toscrape.com/' + book.find('a').attrs['href']

        response = requests.get(current_link)
        book_info = get_info(BeautifulSoup(response.content.decode('utf-8','ignore'), 'html.parser'))
        response.close()
        books.append(book_info)

pprint(books)
# titles = [book['title'] for book in books]
# pprint(list(categories))
# pprint(titles)
