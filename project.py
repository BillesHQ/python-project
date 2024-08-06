from bs4 import BeautifulSoup
import requests

product_page_url = requests.get('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html');
content = product_page_url.text
soup  = BeautifulSoup(content, 'html.parser')

table = soup.select('.product_page .table.table-striped')[0]
upc_code = ''
price_excl_tax = ''
price_incl_tax = ''

for row in table.find_all('tr'):
    if row.find('th').text.upper() == 'UPC':
        upc_code = row.find('td').text
    elif row.find('th').text.upper() == 'PRICE (EXCL. TAX)':
        price_excl_tax = row.find('td').text.replace('Â','').replace('£', '')
    elif row.find('th').text.upper() == 'PRICE (INCL. TAX)':
        price_incl_tax = row.find('td').text.replace('Â','').replace('£', '')

print(upc_code)
print(price_excl_tax)
print(price_incl_tax)

# url = 'https://books.toscrape.com/'
# pages = [url]

# for i in range(2,51):
#     path = 'catalougue/page-' + str(i) + '.html'
#     pages.append(url + path)
# pprint(pages)



# universal_product_code = BeautifulSoup(product_page_url.text, 'html.parser');
# price_excluding_tax = upx
