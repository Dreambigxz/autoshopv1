from craigslistworker import domain
from craigslistworker.save_data import Save

class Searches:
    """
    Class purpose is for reusability of code.
    """
    def __init__(self,
        search, city, section='sss', filters=['&postedToday=1'],
        car_data=False, save_html=False, proxies=None,
        verify=None, is_manual=False):
        self.search = search
        self.section = section
        self.domains, self.city = domain.domain_builder(
            search, section,
            filters, city
        )
        self.car_data = car_data
        self.save_html = save_html
        self.proxies = proxies
        self.verify = verify
        self.is_manual = is_manual

    def compile_search(self):
        return Save(
             domain=self.domains,
             city=self.city,
             search=self.search,
             car_data=self.car_data,
             save_html=self.save_html,
             proxies=self.proxies,
             verify=self.verify,
             is_manual=self.is_manual
             ).save_data()
