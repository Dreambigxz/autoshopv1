from craigslistworker import domain
from app.models import *
import req
from bs4 import BeautifulSoup
from datetime import date, datetime
from device import random_device
import modules
import re
import json
from colorama import Fore, Back, Style
import itertools

class CraigslistSearches:
    """docstring for CraigslistSearches."""

    def __init__(self, domain_get, city='sfbay',
        save_html=True, proxies=None, verify=None):
        super(CraigslistSearches, self).__init__()
        self.page = req.requests.get(
            url=domain_get,
            proxies=proxies,
            verify=verify,
            headers=random_device()
        )
        req.urllibinsecure
        print(f'This page says {self.page}')

        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.save_html = save_html
        self.city = city
        self.proxies = proxies
        self.verify = verify

    def response(self):
        return self.page.status_code

    def save_html(self):
        with open('page/{}_{}.py'.format(datetime.now(), self.city), 'w') as f:
            f.write(self.page.text)

    def result(self):
        return self.soup.find_all(class_='result-info')

    def post_id(self):
        return [i.find(class_='result-title hdrlnk')['id'] for i in self.result()]

    def paginator(self):
        return len(self.result())

    def price(self):
        return [i.find(class_='result-price').text for i in self.result()]

    def title(self):
        return [i.find(class_='result-heading').text for i in self.result()]

    def ad_href(self):
        return [i.find('a').get('href') for i in self.result()]

    def date(self):
        date_time = []
        date = [i.find(class_='result-date')['datetime'] for i in self.result()]
        time = [i.find(class_='result-date')['title'].split()[3].split(':')[2] for i in self.result()]
        for date, time in zip(date, time):
            date_time.append(f'{date}:{time}')
        return date_time

    def location(self):
        location = []
        locations = [i.find(class_='result-hood') for i in self.result()]
        for i in location:
            if location.text is not None:
                location.append(locations)
        print("THis location is", location )
        return location

    def posting_details_per_item(self, urls):
        """
        Retuns an array of all the Posting Details and Description in an array.
        """
        posting_details = []
        description = []
        image_url = []

        for url in [urls]:
            print(f'Running loops for {len([urls])} url1:{urls}')
            ad_page = req.requests.get(
            urls, proxies=self.proxies,
            verify=self.verify,
            headers=random_device(),
            )
            req.urllibinsecure
            print(f'Details page says {ad_page}')

            soup = BeautifulSoup(ad_page.content, 'html.parser')

            ad_info = soup.select('span')
            data = []
            unorganized_data_info = []
            vehicle_options = []
            latitude =[]
            longitude = []

            map = soup.find(id='map')
            map_url = f'https://www.google.com/maps/search/{latitude},{longitude}'

            try:
                latitude.append(map['data-latitude'])
                longitude.append(map['data-longitude'])
            except Exception as e:
                print(Fore.RED+"Could nor load users max, excepted", longitude, latitude)

            print(Fore.LIGHTCYAN_EX+"html-map, and url", map, map_url)

            print(Style.RESET_ALL)


            scripts_tag = [i for i in soup.find_all('script', id='ld_posting_data')]
            urlmatch = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            extract_image_urls = re.findall(urlmatch, str(scripts_tag))
            if len(extract_image_urls) > 0:
                remove_first_item = extract_image_urls.pop(0)

            for info in ad_info:  # only keep elements that don't have a 'class' or 'id' attribute
                if not (info.has_attr('class') or info.has_attr('id')):
                    data.append(info)

            for d in data:
                unorganized_data_info.append(d.text.split(': '))

            description_raw = soup.find_all(id='postingbody')
            veh  = soup.find_all('blockquote')
            print('vehicle_options', veh)
            if len(veh) != 0:
                options = modules.clean_html(str(veh[-1]), '<br/>').split('\n')
                vehicle_options = json.dumps([i.strip() for i in options])
                print(vehicle_options, 'successfully dumped')
                has_vehicle_option = True
            else:
                has_vehicle_option = False

            for item in description_raw:
                unfiltered = item.get_text(strip=True)
                desc = unfiltered.strip('QR Code Link to This Post')
                if has_vehicle_option:
                    description.append(desc.replace(veh[-1].text, ''))
                else:
                    description.append(desc)
            posting_details.append(unorganized_data_info)
            sub_chars = description[0].translate({ord(i): None for i in ['*', '_']})
            description = sub_chars

        return {
            'tags': posting_details[0][1:],
            'image_url':extract_image_urls,
            'description':description,
            'map_url':map_url,
            'vehicle_options': vehicle_options
        }
