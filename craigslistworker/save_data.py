from .worker import CraigslistSearches
from app.models import Car
from datetime import datetime
import itertools
import json
from modules import save_image_from_url, decode
from colorama import Fore, Back, Style


class Save:
    """docstring for SaveData."""
    def __init__(self,
     domain, city, search,
     car_data=True, save_html=False,
     proxies=None, verify=None,
     is_manual=False
     ):
        super(Save, self).__init__()
        self.domain = domain[0]
        self.city = city[0]
        self.save_html = save_html
        self.proxies = None
        self.verify = True
        self.search = search,
        self.is_manual=is_manual,
        if self.search == ' ':
            self.search = None

        print(Fore.GREEN+search)

    def worker(self):
        data = CraigslistSearches(
        self.domain,
        self.city,
        self.save_html,
        self.proxies,
        self.verify,
        )
        return data

    #2022-06-15 16:46
    def treat_date(self, date_time):
            return datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')

    def check_post_id(self):
        r_query = [i.post_id for i in Car.objects.filter(
        which_city=self.city
        )]
        return r_query

    def check_post_date(datetime_worker):
        query_db = [i.datetime for i in Car.objects.filter(
        which_city=self.city
        ).order_by('-datetime')][-0]
        if query_db < datetime_worker and datetime_worker > datetime.datetime -timedelta():
            return True
        else:
            print('We could not save to db because the post is less than {}')
            return False

    def save_data(self):
        temp_date = []
        worker = self.worker()
        looping = 0
        stop_loop = 122
        if self.is_manual == True:
            stop_loop = 3

        if worker.response() != 200:
            return {
            'success': False,
            'status': worker.response()
            }

        print(Fore.GREEN+f'Sending datas Domain, city, proxies, verified-certificate{self.domain, self.city, self.proxies, self.verify}')
        if worker.price() is None:
            print('Cant continue with  this reques')
            exit()

        for (price, title, post_id, url, location, date) in itertools.zip_longest(
            worker.price(), worker.title(),
            worker.post_id(), worker.ad_href(),
            worker.location(), worker.date()
        ):
            if looping >= stop_loop:
                print(Fore.GREEN+"SUCCCES")
                print(Style.RESET_ALL)
                return('success')

            if post_id not in self.check_post_id():

                """
                before entring the details page, check the last
                """
                posting_details = worker.posting_details_per_item(urls=url)

                try:
                    description = posting_details['description']
                except Exception as e:
                    description = None

                image_url = posting_details['image_url']
                print(image_url, '\n', len(image_url))

                try:
                    tag = posting_details['tags']
                    key = [i[-0] for i in tag]
                    val = [i[-1] for i in tag]
                    zip_tags = itertools.zip_longest(key, val)
                    #print('Tags successfully zipped, ready to commit')
                except Exception as e:
                    zip_tags = zip([], [])
                    print(Fore.RED+'Tags are empty')

                saving_image = False
                try:
                    saving_image = image_url.pop(0)
                    #print(Fore.BLUE+f'Saving url: {saving_image}\nTotal thumbnail:{len(image_url)}')
                except Exception as e:
                    saving_image = False
                    print('Image will not be saved, probably no imahe found.')
                saving_image = False

                key = [num for num in range(len(image_url))]
                zip_sub_images = itertools.zip_longest(key, image_url)

                print(Fore.GREEN+ f'Price:{price}\nTitle:{title}')
                temp_date.append(self.treat_date(date))
               	print(Fore.YELLOW+f'Dates: {temp_date}')

                car = Car.objects.create(
                    which_city=self.city,
                    which_area=self.search,
                    title=title,
                    price_string=price,
                    datetime=self.treat_date(date),
                    post_id=post_id,
                    post_url=url,
                    description=description,
                    thumbnails=json.dumps(dict(zip_sub_images)),
                    tags=json.dumps(dict(zip_tags)),
                    location=location,
                    map_url=posting_details['map_url'],
                    vehicle_options=posting_details['vehicle_options']
                )
                car.display_odometer = decode(car.tags)['odometer']
                car.save()

                if saving_image is not False:
                    save_image_from_url(
                     car, saving_image,
                     self.proxies, self.verify
                )

            else:
                print(f'{post_id}, Existed')
                search = Car.objects.get(post_id=post_id)
                if search.which_area is None and self.search != ' ':
                    search.which_area = self.search
                    search.save()
                    print(f'successfully save {self.search} data')

            looping += 1
