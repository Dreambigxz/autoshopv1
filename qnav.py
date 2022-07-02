from main import main
from app.models import Car
from bs4 import BeautifulSoup
from page import details, list
from proxies import proxies

detail = BeautifulSoup(details.details, 'html.parser')
list = BeautifulSoup(list.list, 'html.parser')
urlmatch = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


if __name__ == '__main__':
    main()

def runmain(search='', proxies=proxies, is_manual=True, verify=False):
    main(proxies=proxies, search=search, is_manual=False, verify=verify)
# https://sfbay.craigslist.org/sby/ctd/d/los-banos-2017-chevrolet-chevy-camaro/7500239859.html
