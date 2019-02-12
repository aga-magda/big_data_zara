from zara_functions import *

# saving csv data sets to variables
zara_poland = pd.read_csv("zara_poland.csv", index_col=False, header=0, delimiter=';')
zara_russia = pd.read_csv("zara_russia.csv", index_col=False, header=0, delimiter=';')
zara_singapore = pd.read_csv("zara_singapore.csv", index_col=False, header=0, delimiter=';')
zara_thailand = pd.read_csv("zara_thailand.csv", index_col=False, header=0, delimiter=';')
zara_united_states = pd.read_csv("zara_united_states.csv", index_col=False, header=0, delimiter=';')
zara_zimbabwe = pd.read_csv("zara_zimbabwe.csv", index_col=False, header=0, delimiter=';')

# merge all data sets into one ans save to csv file
merge_data = [zara_poland, zara_russia, zara_singapore, zara_thailand, zara_united_states, zara_zimbabwe]
all_countries = pd.concat(merge_data)#
all_countries.to_csv('all_countries.csv', sep=';', encoding='utf-8', index=False)