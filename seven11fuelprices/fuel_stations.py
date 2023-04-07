from seven11fuelprices.crawler.crawler import FuelPriceWebsite
from seven11fuelprices.json_helper import JsonHelper
from seven11fuelprices.petrol_spy import PetrolSpyClient


class SevenElevenFuelStations:
    crawler = FuelPriceWebsite()
    json = JsonHelper()
    petrolSpyClient = PetrolSpyClient()

    def __init__(self):
        self.locations = self.json.import_json();
        self.petrol_spy = self.json.import_json('petrol_spy');

    def export_fuel_locations(self):
        print("Getting Fuel Prices")
        locations = self.crawler.get_stations()
        JsonHelper().export_json('locations', object=locations)

    def export_petrol_spy(self):
        if self.stations is None or self.stations == False:
            self.export_fuel_locations()
        self.get_petrol_spy_ids()

    def get_petrol_spy_ids(self):
        psDataStations = petrolSpyClient.findStations(self.stations, "SEVENELEVEN");
        filename = self.dir_path + "/data/seven_eleven_petrol_spy.json"
        self.json.export_json(filename, psDataStations)

    def get_staion_ids(self):
        ids = []
        for station in self.petrol_spy.items():
            ids.append(station[1].get("id"))
        return ids

    async def get_price(self, session, id):
        path = f"webservice-1/station/{id}"
        url = self.petrolSpyClient.base_url + path
        async with session.get(url) as resp:
            price_response = await resp.json()
            return self.petrolSpyClient.get_price_from_response(price_response)
