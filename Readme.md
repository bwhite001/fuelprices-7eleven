Australian Fuel Prices for 7-Eleven Franchise
=============================================

This Python package provides an easy way to get a list of Australian fuel prices for 7-Eleven Franchise. The prices are sourced from the [7-Eleven Fuel App](https://www.7eleven.com.au/fuel-app).

Installation
------------

To install the package, you can use `pip`:

bashCopy code

`pip install fuelprices-7eleven`

Usage
-----

To use the package, simply import it and call the `get_prices()` function:

pythonCopy code

`from fuelprices_7eleven import get_prices  prices = get_prices() print(prices)`

The `get_prices()` function returns a list of dictionaries, where each dictionary contains the following keys:

*   `fuel_type`: the type of fuel (e.g. "Unleaded 91", "Premium Unleaded 95", etc.)
*   `price`: the price of the fuel (in cents per litre)
*   `location`: the location of the 7-Eleven store where the fuel price was sourced

Here is an example of the output:

pythonCopy code

`[     {'fuel_type': 'Unleaded 91', 'price': 160, 'location': 'Sydney'},     {'fuel_type': 'Unleaded 91', 'price': 162, 'location': 'Melbourne'},     {'fuel_type': 'Unleaded 91', 'price': 163, 'location': 'Brisbane'},     {'fuel_type': 'Unleaded 91', 'price': 164, 'location': 'Perth'},     {'fuel_type': 'Premium Unleaded 95', 'price': 181, 'location': 'Sydney'},     {'fuel_type': 'Premium Unleaded 95', 'price': 183, 'location': 'Melbourne'},     {'fuel_type': 'Premium Unleaded 95', 'price': 185, 'location': 'Brisbane'},     {'fuel_type': 'Premium Unleaded 95', 'price': 186, 'location': 'Perth'} ]`

You can also pass a location to the `get_prices()` function to get prices for a specific city:

pythonCopy code

`prices = get_prices(location="Melbourne") print(prices)`

This will return a list of fuel prices for 7-Eleven stores in Melbourne.

Contributing
------------

If you find a bug or would like to suggest an improvement, please open an issue on the [GitHub repository](https://github.com/bwhite/fuelprices-7eleven).

If you would like to contribute to the package, please fork the repository, make your changes, and submit a pull request.

License
-------

This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.