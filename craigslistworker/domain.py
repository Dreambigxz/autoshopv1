import csv
import pkg_resources

def domain_builder(search, section, filters, cities):
    """
    Return 0: Array of domains
    Return 1: Array of cities

    Builds the Craigslist URL's for each city in 'city.csv'

    Some options for sorting your craigslist are found below,
    more options can be found in readme.txt and the rest can
    be found simply by going on craigslist.

    Section: 'sss' = all
             'cta' = cars all
             'cto' = cars owner
             'syp' = computer parts
             'sya' = computers
             'ela' = electronics
             'zip' = free stuff
    """

    domains = []
    cities_list = []

    domain_section = section
    domain_search = '?query={}'.format(search)

#    DATA_PATH = pkg_resources.resource_filename('craigslistworker', 'city_data/cities_compile.csv')
#    with open(DATA_PATH) as csv_file:
#        cities = csv.reader(csv_file)
    for city in cities:
        domains.append('https://' + str(city) + '.craigslist.org/search/' + domain_section + domain_search + ''.join(filters))
        cities_list.append(city)
        print(domains, city)
    return domains, cities_list

def which_city(CITIES=[]):
    with open(r'craigslistworker/city_data/craigslist_cities_list.csv') as csv_file:
        cities_data = csv.reader(csv_file)
        cities_list = [i for i in cities_data]
        CITIES.append([(i[0],i[0]) for i in cities_list])
        return CITIES[0]
