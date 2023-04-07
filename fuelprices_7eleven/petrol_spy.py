from seven11fuelprices.crawler.requests import RequestApi
from datetime import datetime, timedelta

class PetrolSpyClient(RequestApi):
    base_url = "https://petrolspy.com.au/"

    def __init__(self):
        super(PetrolSpyClient, self).__init__(self.base_url)

    def getInBox(self,station, lat, long, size=0.05):
        path = "webservice-1/station/box"
        params = {
            'neLat': round(lat + size, 5),
            'neLng': round(long + size, 5),
            'swLat': round(lat - size, 5),
            'swLng': round(long - size, 5),
        }
        jsonResponse = self.json(path, params=params)
        if "message" not in jsonResponse:
            return []
        if "list" not in jsonResponse.get("message") or len(
                jsonResponse.get("message").get("list")) == 0:
            return []
        return jsonResponse.get("message").get("list")

    def findStations(self, stations, brand=None):
        petrolSpyStations = {}
        for station in stations:
            petrolSpyStations.update(self.findStation(station, brand));
            print(str(len(petrolSpyStations))+ "/" + str(len(stations)))
        return petrolSpyStations

    def findStation(self, station, brand=None):
        cords = station.get("coordinates")
        places = {}
        if cords is not None:
            box = self.getInBox(station, cords.get("lat"), cords.get('long'))
            for place in box:
                if place.get("brand") == brand:
                    places[place.get("id")] = place;
        return places;

    def get_price_from_response(self, price_obj):
        result = {
            'name': price_obj.get('name'),
            'lat': price_obj.get('location').get('y'),
            'long': price_obj.get('location').get('x'),
            'state': price_obj.get('state')
        }
        prices = price_obj.get("prices").items();
        now = datetime.now()
        for (fuel,price) in prices:
            updated = datetime.fromtimestamp(int(price.get('updated') / 1000))
            if now-timedelta(hours=24) <= updated <= now:
                result[fuel] = {
                    'type': price.get('type'),
                    'updated': updated
                }
                result[fuel+"_price"] = price.get('amount')
        return result;

