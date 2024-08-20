from bs4 import BeautifulSoup
import requests

# links
product_page_url = requests.get('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html');
content = product_page_url.text
soup  = BeautifulSoup(content, 'html.parser')
book_link = soup.find_all('div',class_='image_container')

# looping through each book


table = soup.select('.product_page .table.table-striped')[0]
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

soup.find_all('a', class_='image_container')

print(title.find('h1').text)
print(number_available)
print(upc_code)
print(price_excl_tax)
print(price_incl_tax)
print(product_description.text)
print(category[2])
print(image_url)
print(review_rating)

# url = 'https://books.toscrape.com/'
# pages = [url]

# for i in range(2,51):
#     path = 'catalougue/page-' + str(i) + '.html'
#     pages.append(url + path)
# pprint(pages)



# universal_product_code = BeautifulSoup(product_page_url.text, 'html.parser');
# price_excluding_tax = upx
