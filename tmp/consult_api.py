# script para consultar API de Mercado Libre

import requests
import json
from datetime import datetime

DATE = str(datetime.date.today()).replace('-', '')
CATEGORY = "MLA1577"

def get_most_relevant_items_for_category(category):
    url = f'https://api.mercadolibre.com/sites/MLA/search?category={category}#json'
    response = requests.get(url).text
    response = json.loads(response)
    data = response("results")
    
    with open('file.tsv', 'w') as file:
        for item in data:
            _id = get_key_from_item(item, 'id')
            site_id = get_key_from_item(item, 'site_id')
            title = get_key_from_item(item, 'title')
            price = get_key_from_item(item, 'price')
            sold_quantity = get_key_from_item(item, 'sold_quantity')
            thumbnail = get_key_from_item(item, 'thumbnail')

            file.write(f"{_id}\t{site_id}\t{title}\t{price}\t{sold_quantity}\t{thumbnail}\t{DATE}\n")

def get_key_from_item(item, key):
    return str(item[key]).replace(' ', '').strip() if item.ket(key) else "null"

def main():
    get_most_relevant_items_for_category(CATEGORY)