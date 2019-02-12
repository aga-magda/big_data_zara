from zara_functions import*


# SALE PRODUCTS #
# Getting started
sale_link = 'https://www.zara.com/sg/en/sale-l879.html?v1=792612'
regular_link = 'https://www.zara.com/sg/en/new-collection-l1580.html?v1=1162518'
results = ''
currency = 'S$ '
exchange_rate = 2.7321
country = 'Singapore'

# Getting sale products
results = getting_sale_products(sale_link, results, currency, exchange_rate, country)


# REGULAR PRODUCTS #
results = getting_regular_products(regular_link, results, currency, exchange_rate, country)


# save data to csv
header = 'master_category; subcategory; product_id; product_name; product_regular_price; product_regular_price_pln; product_promo_price; product_promo_price_pln; country' + '\n'

file = open(os.path.expanduser('zara_singapore.csv'), 'wb')
file.write(bytes(header, encoding='utf-8'))
file.write(bytes(results, encoding='utf-8'))
