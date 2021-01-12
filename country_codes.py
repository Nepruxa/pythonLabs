import json

from bs4 import BeautifulSoup
import requests

country_url = 'https://www.iban.com/country-codes'


def parse_countries(url):
    raw_html = requests.get(url)
    soup = BeautifulSoup(raw_html.text, 'html.parser')
    table = soup.find('table', class_='table table-bordered downloads tablesorter')
    country_str = table.find_all('tr')
    country_dict = {}
    for item in country_str:
        country_dict.update({item.contents[1].text: item.contents[3].text})  # TODO: Catch Unicode Å symbol
    del country_dict['Country']
    return country_dict


with open('countries.json', 'w', encoding='utf-8') as countries_json:
    json.dump(parse_countries(country_url), countries_json)
countries_json.close()
