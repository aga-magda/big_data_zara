from zara_functions import*


# SALE PRODUCTS #
# Getting started
sale_link = 'https://www.zara.com/ru/en/sale-l879.html?v1=643502'
regular_link = 'https://www.zara.com/ru/en/new-collection-l1580.html?v1=1163061'
results = ''
currency = ' руб'
exchange_rate = 0.0499
country = 'Russia'

# Getting sale products
results = getting_sale_products(sale_link, results, currency, exchange_rate, country)


# REGULAR PRODUCTS #
results = getting_regular_products(regular_link, results, currency, exchange_rate, country)


# save data to csv
header = 'master_category; subcategory; product_id; product_name; product_regular_price; product_regular_price_pln; product_promo_price; product_promo_price_pln; country' + '\n'

file = open(os.path.expanduser('zara_russia.csv'), 'wb')
file.write(bytes(header, encoding='utf-8'))
file.write(bytes(results, encoding='utf-8'))



