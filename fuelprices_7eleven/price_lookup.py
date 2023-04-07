import asyncio
import time

import aiohttp

from fuelprices_7eleven.fuel_stations import SevenElevenFuelStations

sevenElevenFuelStationsClient = SevenElevenFuelStations()

class LookupPrices:
    types = ['E10', 'U91', 'U95', 'U98', 'PremDSL', 'AdBlue']
    start_time = time.time()

    def __init__(self, top=3):
        self.top = top;

    def all(self):
        asyncio.run(self.load())
        print("--- %s seconds ---" % (time.time() - self.start_time))
        return self.items

    def get_top(self, top=0):
        asyncio.run(self.load())
        if top == 0:
            top = self.top
        cheep = {}
        for type in self.types:
            cheep[type] = [];
            sorted_price = self.items[type]
            for cheep_price in sorted_price[0:top]:
                cheepest = {
                    'name': cheep_price.get('name') + " " + cheep_price.get(
                        "state"),
                    'location': f"{cheep_price.get('lat')},{cheep_price.get('long')}",
                    'price': cheep_price.get(type + '_price'),
                    'updated': cheep_price.get(type).get('updated'),
                }
                cheep[type].append(cheepest)
        self.items = cheep.items()

    async def load(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            station_ids = sevenElevenFuelStationsClient.get_staion_ids()
            for station in station_ids:
                tasks.append(
                    asyncio.ensure_future(
                        sevenElevenFuelStationsClient.get_price(
                            session, station)
                    )
                )
            items = {}
            prices = await asyncio.gather(*tasks)
            for type in self.types:
                items[type] = []
                key = type + "_price"
                items[type] = sorted((i for i in prices if key in i),
                                      key=lambda k: k[key])
            self.items = items
            return self.items;