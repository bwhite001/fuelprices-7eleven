import json
import os

class JsonHelper:
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    filenames = {
        'locations': "data/seven_eleven_locations.json",
        'petrol_spy': "data/seven_eleven_petrol_spy.json",
        'django_fuel_station': "data/seven_eleven_petrol_spy.json",
        'django_fuel_price_station': "data/seven_eleven_petrol_spy.json",
    }
    def get_export_path(self, index='locations'):
        if(index is None):
            index = "locations"
        return self.dir_path + "/" + self.filenames.get(index);

    def export_json(self, path, object):
        filename = self.get_export_path(path);
        # Serializing json
        json_object = json.dumps(object, indent=4)
        with open(filename, "w") as outfile:
            outfile.write(json_object)
        print(f"Exported {len(object)} {path}: to {filename}")

    def import_json(self, path=None):
        if path is None:
            path = 'locations'
        filename = self.get_export_path(path);
        if (not os.path.exists(filename)):
            print(f"Unable to locate file: {filename}")
            return False
        # Opening JSON file
        f = open(filename)
        # returns JSON object as
        # a dictionary
        data = json.load(f)
        # Closing file
        f.close()
        print(f"imported {len(data)} {path}: from {filename}")
        return data;