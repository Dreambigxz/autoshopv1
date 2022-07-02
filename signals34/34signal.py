import csv
import pkg_resources
from craigslistworker.search import Searches
# from .models import CrawlerAgent, CitiesTOScrab
import time
from modules import decode

class SendWorkerSignal:
    """docstring for SendWorkerSignal."""

    """
     THis is responsible of looping through the assigned cities and send to signal the Search
     1. 34SIGNALS ---
     2. Searches ++++
            sends to domain to build the url and return the url built based on the first city on the list
     3. Domain Builds up return
     4. send all searches data to save_data
            The save data sends all signal to worker, while  worker sends all quiries to Craigslist dot com:

            [


            ]

    """

    def __init__(self):
        super(SendWorkerSignal, self).__init__()

    def reload_citities(self, cities=[]):
        citites = pkg_resources.resource_filename('craigslistworker', 'city_data/cities_compile.csv')
        with open(cities) as csv_file:
            read_cities_from_csv_path = csv.reader(csv_file)
            cities.append([i for i in cities_data])
            #definitely thois would commit everthing backk to db and return the decode object to next availableuser

        return cities


    def users(self is_active=False):
        #only filter users that has status not active by default
        users = CrawlerAgent.objects.Filter(is_active=False)
        if users.count() >= 1
            user = self.user(is_active=False)[0]
        else:
            user = None
        return user

    def cities_to_crawl():
        # get all available cities to crawl
        citites = CitiesTOScrab.objects.all()[0]
        user = self.users()
        if user is not None:
            user.is_active = True
            user.save()

            while cities.is_lock:
                time.sleep(5)
            else:
                """
                    By default a user could take 100, 200, 300, at a time
                """
                list_cities_to_scrab = decode(cities.cities)
                cities.is_lock = True
                cities.save()

                if len(list_cities_to_scrab) <= 100:
                    #reload_citities and make sure the left datas come fires
                    hold_left_datas = []+list_cities_to_scrab
                    list_cities_to_scrab = reload_citities()
                    # if len(hold_left_datas) in range(59, 86):
                    #     stop_index 60
                    #     my_city = list_cities_to_scrab[0:stop_index] +hold_left_datas
                    # elif len(hold_left_datas) in ran

                        stop_index = 50
                        my_city = list_cities_to_scrab[0:stop_index] +hold_left_datas
                    else:
                        print('somthing else happend at block reload_citities')
                else:
                    if len(list_cities_to_scrab) <= 140:
                        stop_index = len(list_cities_to_scrab)
                        my_city = cities[0:stop_index]
                    else
                        stop_index = 150
                        my_city = list_cities_to_scrab[0:stop_index]

                    cities = json.dumps(list_cities_to_scrab[stop:])
                    cities.is_lock = False
                    cities.save()

                """
                Now we successfully got a list of cities to loop and commit to data base by a user.
                Saved back the remaining cities list to db.
                Return  users

                """
