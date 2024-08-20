from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests
current_link = 'https://books.toscrape.com/index.html'
product_page_url = requests.get(current_link).text;
soup  = BeautifulSoup(product_page_url, 'html.parser')
links = soup.find_all('div',class_='image_container')
# functions to get information

def get_info(soup):

    table = soup.select('.product_page .table.table-striped')[0]
    table_body = table.find('tbody')
    title = soup.select('.col-sm-6.product_main')[0]
    upc_code = ''
    price_excluding_tax = ''
    price_including_tax = ''
    number_available_element = soup.select('.instock.availability')[0]
    number_available = ''.join(filter(str.isdigit, str(number_available_element)))
    product_description = soup.select('#product_description + p')[0]
    category = soup.select('.breadcrumb')[0].text.split()
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    image_url = soup.select('.product_page .item.active')[0].find('img').attrs['src']

    for row in table.find_all('tr'):
      if row.find('th').text.upper() == 'UPC':
          upc_code = row.find('td').text
      elif row.find('th').text.upper() == 'PRICE (EXCL. TAX)':
          price_excl_tax = row.find('td').text.replace('Â','').replace('£', '')
      elif row.find('th').text.upper() == 'PRICE (INCL. TAX)':
          price_incl_tax = row.find('td').text.replace('Â','').replace('£', '')

    print('title: ' + title.find('h1').text + '\n')
    print('Available Books: ' + number_available + '\n')
    print('UPC Code: ' + upc_code + '\n')
    print('Price Excluding Tax: ' + price_excl_tax + '\n')
    print('Price Including Tax: ' + price_incl_tax + '\n')
    print('Description: ' + product_description.text + '\n')
    print('Category: ' + category[2] + '\n')
    print('Image URL' + image_url + '\n')
    print('Book Rating: ' + review_rating + '\n')

for book in links:
  current_link = 'https://books.toscrape.com/' + book.find('a').attrs['href']
  print(current_link + '\n' + '\n')
  get_info(BeautifulSoup(requests.get(current_link).text, 'html.parser'))

# url = 'https://books.toscrape.com/'
# pages = [url]

# for i in range(2,51):
#     path = 'catalougue/page-' + str(i) + '.html'
#     pages.append(url + path)
# pprint(pages)



# universal_product_code = BeautifulSoup(product_page_url.text, 'html.parser');
# price_excluding_tax = upx
