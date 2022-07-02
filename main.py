from craigslistworker.searches import Searches
from craigslistworker.city_data import readw
from proxies import proxies
import time
#from app.views import *

def main(
    city='sfbay',
    car_data=True,
    extra_filters='',
    is_manual=False,
    search='',
    proxies=None,
    verify=True,
    save_html=False,
    ):
    #print(search, extra_filters, city)
    """
    Define searches here, a few examples are given below.
    search_name = searches.Searches('your search', 'section')
    default section is 'sss' which is all of craigsli`st.
    """
    filters=['&postedToday=1']
    search = Searches(
      search=search, city=[city], section='cta',
      filters=filters, car_data=car_data, save_html=save_html,
       proxies=proxies, verify=verify, is_manual=is_manual

     )
    start_serach = search.compile_search()
    return start_serach

if __name__ == '__main__':
    main()
    print(time.perf_counter())
