from pprint import pprint
# from bs4 import BeautifulSoup
# import requests

# product_page_url = requests.get('https://books.toscrape.com/');

url = 'https://books.toscrape.com/'
pages = [url]

for i in range(2,51):
    path = 'catalougue/page-' + str(i) + '.html'
    pages.append(url + path)
pprint(pages)



# universal_product_code = BeautifulSoup(product_page_url.text, 'html.parser');

# # price_excluding_tax = upx
