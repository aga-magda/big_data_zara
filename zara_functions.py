from bs4 import BeautifulSoup
import pandas as pd
import requests
import os


def getting_sale_products(sale_link, results, currency, exchange_rate, country):
    subcategories_dict = {}

    r = requests.get(sale_link)
    r.raise_for_status()
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    # Getting all subcategories for woman
    master_category = soup.find('li', {'data-name': 'SALE'})
    category = master_category.find('li', {'data-name': 'WOMAN'})
    subcategories = category.find('ul')
    for s in subcategories:
        subcategory_name = s.findChildren()[0].text.strip()
        # subcategory link:
        if s.findChildren()[0].has_attr('href'):
            subcategory_link = s.findChildren()[0]['href']
        else:
            subcategory_link = s.findChildren()[0]['data-href']

        subcategories_dict[subcategory_name] = subcategory_link
    print(subcategories_dict)

    # Iterating through subcategories
    for s in subcategories_dict:
        r = requests.get(subcategories_dict[s])
        r.raise_for_status()
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        products = soup.findAll('li', {'class': 'product'})

        for p in products:
            product_info_tag_not_empty = p.find('div', {'class': 'product-info'}).text
            if product_info_tag_not_empty:
                product_id = p['data-productid']
                product_name = p.find('a', {'class': 'name'}).text

                if p.find('span', {'class': 'line-through'}):
                    product_regular_price = p.find('span', {'class': 'line-through'})['data-price'].split(currency)[0].replace(',', '.')
                    product_promo_price = p.find('span', {'class': 'sale'})['data-price'].split(currency)[0].replace(',', '.')
                    product_regular_price_pln = float(product_regular_price)
                    product_promo_price_pln = float(product_promo_price)
                    country = country

                    if not currency == ' PLN':
                        product_regular_price_pln = float(product_regular_price) * exchange_rate
                        product_promo_price_pln = float(product_promo_price) * exchange_rate

                    one_result = 'SALE;' + s + ';' + product_id + ';' + product_name + ';' + product_regular_price +\
                                 ';' + str(round(product_regular_price_pln, 2)) + ';' + product_promo_price + ';' + \
                                 str(round(product_promo_price_pln, 2)) + ';' + country + '\n'
                    results = results + one_result
    return results


def getting_regular_products(regular_link, results, currency, exchange_rate, country):
    # Getting started
    subcategories_dict = {}

    r = requests.get(regular_link)
    r.raise_for_status()
    html = r.text
    soup = BeautifulSoup(html, 'lxml')

    # Getting all subcategories for woman
    master_category = soup.find('li', {'data-name': 'NEW COLLECTION'})
    category = master_category.find('li', {'data-name': 'WOMAN'})
    subcategories = category.find('ul')


    for s in subcategories:
        subcategory_name = s.findChildren()[0].text.strip()
        # subcategory link:
        if s.findChildren()[0].has_attr('href'):
            subcategory_link = s.findChildren()[0]['href']
            data_extraquery = s.findChildren()[0]['data-extraquery']
            subcategory_link = subcategory_link + '?' + data_extraquery
        else:
            subcategory_link = s.findChildren()[0]['data-href']
            data_extraquery = s.findChildren()[0]['data-extraquery']
            subcategory_link = subcategory_link + '?' + data_extraquery

        subcategories_dict[subcategory_name] = subcategory_link

    print(subcategories_dict)

    # Iterating through subcategories
    for s in subcategories_dict:
        r = requests.get(subcategories_dict[s])
        r.raise_for_status()
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
        products = soup.findAll('li', {'class': 'product'})

        for p in products:
            product_info_tag_not_empty = p.find('div', {'class': 'product-info'}).text
            if product_info_tag_not_empty:
                product_id = p['data-productid']
                product_name = p.find('a', {'class': 'name'}).text
                product_regular_price = p.find('div', {'class': 'price'}).span['data-price'].split(currency)[0].replace(',', '.')
                product_promo_price = ''
                product_regular_price_pln = float(product_regular_price)
                product_promo_price_pln = product_promo_price
                country = country

                if not currency == ' PLN':
                    product_regular_price_pln = float(product_regular_price) * exchange_rate
                    product_promo_price_pln = product_promo_price

                one_result = 'NEW COLLECTION;' + s + ';' + product_id + ';' + product_name + ';' + product_regular_price + \
                             ';' + str(round(product_regular_price_pln, 2)) + ';' + product_promo_price + ';' + \
                             str(product_promo_price_pln) + ';' + country +'\n'
                results = results + one_result

    return results
