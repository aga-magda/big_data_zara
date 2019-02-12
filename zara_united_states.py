from zara_functions import*


# SALE PRODUCTS #
# Getting started
sale_link = 'https://www.zara.com/us/en/woman-l1000.html?v1=437525'
regular_link = 'https://www.zara.com/us/en/new-collection-l1580.html?v1=1162573'
results = ''
currency = ' USD'
exchange_rate = 3.7471
country = 'United States'

# Getting sale products
results = getting_sale_products(sale_link, results, currency, exchange_rate, country)


# REGULAR PRODUCTS #
results = getting_regular_products(regular_link, results, currency, exchange_rate, country)


# save data to csv
header = 'master_category; subcategory; product_id; product_name; product_regular_price; product_regular_price_pln; product_promo_price; product_promo_price_pln; country' + '\n'

file = open(os.path.expanduser('zara_united_states.csv'), 'wb')
file.write(bytes(header, encoding='utf-8'))
file.write(bytes(results, encoding='utf-8'))




