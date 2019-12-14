import requests
from bs4 import BeautifulSoup as Soup
from csv import writer
import time
from random import randint

#Constants across Stores
column_headers = ['Store', 'PRODUCT NAME', 'CLOTHING CATEGORY', 'PRICE', 'DESCRIPTION', 'Product Page URL',	'STATIC IMAGE URL']


#Store Anthropologie

#Constants across Store Anthropologie
store = 'Anthropologie'

with open('Anthropologie.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(column_headers)

    ##Jeans
    print('Processing Catagory Jeans')
    anth_jeans_url = 'https://www.anthropologie.com/shop-all-jeans'
    anthpage = '?page='
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    anth = requests.get(anth_jeans_url, headers=headers)
    soup = Soup(anth.text,'html.parser')
    pages = int(soup.find_all('li', text=True)[2].get_text().replace('  ', ''))
    jeans = soup.find_all(class_='dom-product-tile c-product-tile c-product-tile--regular c-product-tile js-product-tile')
    category = 'Jeans'

    #Jeans Page 1
    print('Processing Page #1')
    for jean in jeans:
        sleeping = randint(1,20)
        product_name = jean.find(class_='c-product-tile__h3 c-product-tile__h3--regular').get_text().replace('  ', '').replace('\n', '')
        current_cost = jean.find(class_='c-product-meta__current-price').get_text().replace('  ', '').replace('\n', '')
        product_page_url = 'https://www.anthropologie.com' + jean.find('a')['href']
        image_url = jean.find('img')['src'].replace('//', 'https://')
        jean_request = requests.get(product_page_url, headers=headers)
        jean_prod_page = Soup(jean_request.text,'html.parser')
        jean_description = jean_prod_page.find_all('p', text=True)[4].get_text().replace('  ', '')
        csv_writer.writerow([store, product_name, category, current_cost, jean_description, product_page_url, image_url])
        
        #column_headers = ['Store', 'PRODUCT NAME', 'CLOTHING CATEGORY', 'PRICE', 'DESCRIPTION', 'Product Page URL', 'STATIC IMAGE URL']
        #print(jean_description)
        #print(product_name)
        #print(current_cost)
        #print(category)
        #print(image_url)
        #print(product_page_url)
        #print('Sleeping - ' + str(sleeping))
        time.sleep(sleeping)

    #Jeans Page 2+
    if pages > 2:
        for i in range(2, pages):
            print('Processing Page #' + str(i))
            anth_jeans_url = 'https://www.anthropologie.com/shop-all-jeans' + str(anthpage) + str(i)
            anth = requests.get(anth_jeans_url, headers=headers)
            soup = Soup(anth.text,'html.parser')
            pages = int(soup.find_all('li', text=True)[2].get_text().replace('  ', ''))
            jeans = soup.find_all(class_='dom-product-tile c-product-tile c-product-tile--regular c-product-tile js-product-tile')
            for jean in jeans:
                sleeping = randint(1,20)
                product_name = jean.find(class_='c-product-tile__h3 c-product-tile__h3--regular').get_text().replace('  ', '').replace('\n', '')
                current_cost = jean.find(class_='c-product-meta__current-price').get_text().replace('  ', '').replace('\n', '')
                product_page_url = 'https://www.anthropologie.com' + jean.find('a')['href']
                image_url = jean.find('img')['src'].replace('//', 'https://')
                jean_request = requests.get(product_page_url, headers=headers)
                jean_prod_page = Soup(jean_request.text,'html.parser')
                jean_description = jean_prod_page.find_all('p', text=True)[4].get_text().replace('  ', '')
                csv_writer.writerow([store, product_name, category, current_cost, jean_description, product_page_url, image_url])
                #column_headers = ['Store', 'PRODUCT NAME', 'CLOTHING CATEGORY', 'PRICE', 'DESCRIPTION', 'Product Page URL', 'STATIC IMAGE URL']
                #print(jean_description)
                #print(product_name)
                #print(current_cost)
                #print(category)
                #print(image_url)
                #print(product_page_url)
                #print('Sleeping - ' + str(sleeping))
                time.sleep(sleeping)

    