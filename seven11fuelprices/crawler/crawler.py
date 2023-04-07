import ast
import re
from bs4 import BeautifulSoup
import cloudscraper

class FuelPriceWebsite():
    _url = "https://fuelprice.io/"
    _params = {
        'fuel_type': 'ulp91',
        'state': '',
        'orderby': 'price',
        'order': 'ASC'
    }

    def __init__(self, fuel_type='ulp91', brand='7-eleven'):
        if(brand is not None):
            self._url = self._url+"brands/"+brand+'/'
        self._params['fuel_type'] = fuel_type;

    def initlize(self):
        self.scraper = cloudscraper.create_scraper()
        self.soup = self.makeRequest()

    def get_stations(self):
        script = self.crawler.crawl()
        featureCollection = self.get_json(script)
        return self.get_stations_locations(script)


    def makeRequest(self):
        try:
            page = self.scraper.get(self._url, params=self._params)
            soup = BeautifulSoup(page.content, 'html.parser')
            return soup
        except Exception as ins:
            print(ins)
            sys.exit()

    def crawl(self):
        self.initlize();
        script = self.soup.select("#fuel-map > script")[0].prettify()
        return script

    def get_json(self, script):
        p = re.findall('var geojson=(.+?)\n', script)
        if len(p) == 1:
            geojson = p[0]
            return ast.literal_eval(geojson)

    def get_stations_locations(self, featureCollection):
        stations = []
        for feature in featureCollection['features']:
            station = {}
            station['name'] = feature['properties']['title']
            coordinates = feature['geometry']['coordinates']
            station['coordinates'] = {
                'lat': coordinates[1],
                'long': coordinates[0]
            }
            google_uri = feature['properties']['title'].replace(" ", "+");
            station['suburb'] = feature['properties']['title'].replace("7-Eleven ",
                                                                       "").upper()
            stations.append(station)
        stations = sorted(stations, key=lambda item: item['suburb']);
        return stations;