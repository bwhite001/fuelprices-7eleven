"""
This script retrieves the current fuel prices for the top 1 7-Eleven stores in Australia, and posts them to a Discord webhook. The webhook URL is specified as the `DISCORD_WEBHOOK_URL` environment variable.

The script uses the `LookupPrices` class from the `fuelprices_7eleven.price_lookup` module to retrieve the fuel prices. The `Discord` class from the `discordwebhook` module is used to post the prices to the webhook.

Usage:
    Run the script from the command line. The `DISCORD_WEBHOOK_URL` environment variable must be set to the URL of the Discord webhook that the prices will be posted to.

Dependencies:
    - `click`
    - `tabulate`
    - `discordwebhook`
    - `dotenv`
"""

import click
import os
from tabulate import tabulate

from fuelprices_7eleven.price_lookup import LookupPrices
from discordwebhook import Discord
from dotenv import load_dotenv

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", None)


@click.command()
def run():
    """
    Retrieves the current fuel prices for the top 1 7-Eleven stores in Australia and posts them to a Discord webhook.

    The webhook URL is specified as the `DISCORD_WEBHOOK_URL` environment variable. This function first checks that the variable is set, and raises an exception if it is not.

    The function uses the `LookupPrices` class from the `fuelprices_7eleven.price_lookup` module to retrieve the fuel prices. The `Discord` class from the `discordwebhook` module is used to post the prices to the webhook.

    Returns:
        None

    Raises:
        AssertionError: If the `DISCORD_WEBHOOK_URL` environment variable is not set.

    Dependencies:
        - `fuelprices_7eleven.price_lookup.LookupPrices`
        - `discordwebhook.Discord`"""

    assert (
        DISCORD_WEBHOOK_URL is not None
    ), "You must provide a discord webhook url as ENV variable DISCORD_WEBHOOK_URL"
    lookupPrices = LookupPrices()
    discord = Discord(url=DISCORD_WEBHOOK_URL)
    lookupPrices.get_top(1)
    for type, data in lookupPrices.items:
        if len(data) > 0:
            message = f"\n***{type}***\n"
            for row in data:
                message += f"${row.get('price')} : {row.get('name')} __{row.get('location')}__ \n"
                message += f"\nhttps://www.google.com/maps/search/?api=1&query={row.get('location')}\n"
            discord.post(content=message)


if __name__ == "__main__":
    run()
