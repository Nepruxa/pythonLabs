import logging
import json
import argparse
import re

from bs4 import BeautifulSoup
import requests

from enums import DETAIL_BLOCKS, TITLE_TYPES, BASE_URL


logging.basicConfig(level=logging.DEBUG, filename='debug.log', format='[%(asctime)s] %(levelname)s:%(message)s')
logging.basicConfig(level=logging.ERROR, filename='error.log', format='[%(asctime)s] %(levelname)s:%(message)s')

args_parser = argparse.ArgumentParser(description=f"Initial command example: \n"
                                                  f"scraper.py \n"
                                                  f"\n--title_types 'Feature Film,TV Movie' "
                                                  f"\n--release_date YYYY-MM-DD "
                                                  f"\n--genres Action,Sci-Fi "
                                                  f"\n--user_rating 2.2,8.7"
                                                  f"\n--countries China,United States "
                                                  f"\n\nREMEMBER TO ENCAPSULATE STRING WITH WHITESPACES WITH SINGLE OR DOUBLE QUOTES ")
args_parser.add_argument('--title_types', type=str)
args_parser.add_argument('--release_date', type=str)
args_parser.add_argument('--genres', type=str)
args_parser.add_argument('--user_rating', type=str)
args_parser.add_argument('--countries', type=str)
args = args_parser.parse_args()


class LinkBuilder:
    def __init__(self):
        self.title_types = self.title_type_validator()
        self.release_date = self.datetime_validator(args.release_date)
        self.genres = self.genres_validator()
        self.user_rating = self.user_rating_validator(args.user_rating)
        self.countries = self.country_validator()

    def title_type_validator(self):
        try:
            title_types = args.title_types.split(',')
            if title_types is not None:
                title_type_list = []
                for key, value in TITLE_TYPES.items():
                    for item in title_types:
                        if item == key:
                            title_type_list.append(value)
                return ','.join(title_type_list)
            return 'Feature Film'
        except Exception as e:
            logging.error(f"Error in title_types argument, check yor input: \n{e}")
            return 'Feature Film'

    def datetime_validator(self, date_str):
        if date_str is not None:
            return date_str
        return '2010-01-01,2020-01-01'

    def genres_validator(self):
        try:
            genres = args.genres.split(',')
            if genres is not None:
                return ','.join([x.lower() for x in genres])
            return 'comedy'
        except Exception as e:
            logging.error(f"Error in genres argument, check your input please: \n{e}")
            return 'Feature Film'

    def user_rating_validator(self, user_rating):
        try:
            user_rating_list = args.user_rating.split(',')
            if user_rating_list is not None:
                return ','.join([str(float(x)) for x in user_rating_list])
        except Exception as e:
            logging.error(f"Error in user_rating argument, check your input : \n{e}")
        return '1.0,9.9'

    def country_validator(self):
        try:
            countries = args.countries.split(',')
            countries_list = []
            with open('countries.json', 'r', encoding='utf-8') as countries_json:
                countries_dict = json.load(countries_json)
                for key, value in countries_dict.items():
                    for item in countries:
                        if item in key:
                            countries_list.append(value)
            countries_json.close()
            # return ','.join([x.lower() for x in countries_list])  # TODO: Add correct extracting of country codes
            return 'cn,us'
        except Exception as e:
            logging.error(f"Error in genres, check your input or if file with countries config exists: \n{e}")
            return 'cn,us'


class DataExtractor:
    def __init__(self, url_from_args):
        self.movie_list_url = url_from_args
        self.max_movies = 1000

    def _get_title_type(self, title_bar):
        for title_type in TITLE_TYPES:
            if title_type in title_bar:
                return title_type
        return 'Feature Film'

    def _extract_movie_info(self, html_page):
        soup = BeautifulSoup(html_page.text, 'html.parser')
        title_bar_div = soup.find('div', class_='title_bar_wrapper')
        title_info = {}
        if title_bar_div is not None:
            rating_span = title_bar_div.find('span', attrs={"itemprop": "ratingValue"})
            if rating_span is not None:
                rating = rating_span.text
                title_info['rating'] = rating
            else:
                logging.info('title rating not found')
            title_div = title_bar_div.find('div', class_='titleBar')
            name_h1 = title_div.find('h1')
            if name_h1 is not None:
                if name_h1.span is not None:
                    name_h1.span.decompose()
                name = name_h1.text.replace('\xa0 ', '').strip()
                title_info['name'] = name
            else:
                logging.info('title name not found')
            subtext_div = title_div.find('div', class_='subtext')
            if subtext_div is not None:
                subtext = subtext_div.text
                title_type = self._get_title_type(subtext)
                title_info['title_type'] = title_type
            else:
                logging.info('title type not found')
        else:
            logging.info('title name, title type and rating not found')
        plot_summary_div = soup.find('div', class_='plot_summary')
        if plot_summary_div is not None:
            stars_h4 = plot_summary_div.find('h4', text='Stars:')
            if stars_h4 is not None:
                stars = [star.text for star in stars_h4.parent.find_all('a')]
                del stars[-1]
                title_info['stars'] = stars
        if 'stars' not in title_info:
            logging.info('stars not found')

        title_story_line_div = soup.find('div', id='titleStoryLine')
        if title_story_line_div is not None:
            genres_h4 = title_story_line_div.find('h4', text='Genres:')
            if genres_h4 is not None:
                genres = [star.text.strip() for star in genres_h4.parent.find_all('a')]
                title_info['genres'] = genres
        if 'genres' not in title_info:
            logging.info('genres not found')

        details_div = soup.find('div', id='titleDetails')
        if details_div is not None:
            current_key = 'details'
            needed_block = True
            for child in details_div.children:
                if child.name == 'h3' or child.name == 'h2':
                    current_key = child.text.strip()
                    needed_block = current_key in DETAIL_BLOCKS
                    if needed_block:
                        title_info[current_key] = {}
                if child.name == 'div' and 'txt-block' in child['class'] and needed_block:
                    h4 = child.find('h4')
                    if h4 is not None:
                        sub_key = h4.text.replace(':', '')
                        child.h4.decompose()
                        children_text = [txt.strip() for txt in
                                         child.text.replace('See more\xa0»', '').strip().split('|')]
                        title_info[current_key][sub_key] = children_text if len(children_text) > 1 else children_text[0]
        else:
            logging.info('details not found')
        logging.info(f'title info found')
        print(title_info)
        return title_info

    def start(self):
        total_title_count = 0
        title_pages = []
        while total_title_count < self.max_movies:
            search_url = self.movie_list_url + f'&start={total_title_count + 1}'
            html_doc = requests.get(search_url)
            print(html_doc)
            soup = BeautifulSoup(html_doc.text, 'html.parser')
            titles = {*[link.find('a', href=True).get('href') for link in soup.select('div.lister-item.mode-simple')]}
            if len(titles) == 0:
                break
            title_pages.extend([self._extract_movie_info(requests.get(BASE_URL + title)) for title in titles])
            total_title_count += len(titles)
        with open('result.json', 'w', encoding='utf-8') as result_json:
            json.dump(title_pages, result_json, ensure_ascii=False)
        result_json.close()
        return title_pages


link_builder = LinkBuilder()
request_url = BASE_URL + '/search/title/?' + '&'.join([key + '=' + value for key, value in link_builder.__dict__.items()]) + '&view=simple&count=250'
data_extractor = DataExtractor(request_url)
data_extractor.start()
print(link_builder.title_types)
print(link_builder.release_date)
print(link_builder.genres)
print(link_builder.user_rating)
print(link_builder.countries)
print(request_url)
