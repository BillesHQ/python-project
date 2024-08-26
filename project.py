from bs4 import BeautifulSoup
import requests
from pprint import pprint

home_link = 'https://books.toscrape.com/index.html'
url = 'https://books.toscrape.com/'
categories = set()
page_links = []

for i in range(1,51):
    path = 'catalogue/page-' + str(i) + '.html'
    page_links.append(url + path)
# functions to get information
books = {}

def get_info(soup):

    table = soup.select('.product_page .table.table-striped')[0]
    table_body = table.find('tbody')
    title = soup.select('.col-sm-6.product_main')[0].find('h1').text
    upc_code = ''
    price_excluding_tax = ''
    price_including_tax = ''
    number_available_element = soup.select('.instock.availability')[0]
    number_available = ''.join(filter(str.isdigit, str(number_available_element)))

    product_description_results = soup.select('#product_description + p')
    product_description = ''
    if len(product_description_results) > 0:
        product_description = product_description_results[0].text
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

    return book

# print(links)
# print(pages)
# exit()
c = 20
for page_link in page_links:
    # print(page_link)
    page_response = requests.get(page_link)
    # print(page_response.text)
    soup  = BeautifulSoup(page_response.text, 'html.parser')
    page_response.close()
    book_links = soup.find_all('div',class_='image_container')
    # if c  == 0:
    #     break
    # c -=1
    for book_link in book_links:
        current_link = 'https://books.toscrape.com/catalogue/' + book_link.find('a').attrs['href']
        print(current_link)
        response = requests.get(current_link)
        book_info = get_info(BeautifulSoup(response.content.decode('utf-8','ignore'), 'html.parser'))
        response.close()
        book_category = book_info['Category']
        books_in_category = books.get(book_category, [])
        books_in_category.append(book_info)
        books[book_category] = books_in_category
        # books.append(book_info)
        # print(book_info['title'])
    # break

for category,list in books.items():
    pprint(books.items())
pprint(books)
# titles = [book['title'] for book in books]
# pprint(list(categories))
# pprint(titles)

# for i in books:
#     print(i['Category'])
