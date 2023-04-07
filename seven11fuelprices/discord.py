import click
from tabulate import tabulate

from seven11fuelprices.price_lookup import LookupPrices
from discordwebhook import Discord

@click.command()
def run():
    lookupPrices = LookupPrices()
    discord = Discord(
        url="https://discord.com/api/webhooks/1089851654750351402/BFvJL5ke_HLZ5DHtUTqtcWpQ4LCtG8q5pYmOcSspW4NtfgTS_H1-WQF6ToCI6hYzrlqI")
    lookupPrices.get_top(1)
    for type, data in lookupPrices.items:
        if len(data) > 0:
            message = f"\n***{type}***\n"
            for row in data:
                message += f"${row.get('price')} : {row.get('name')} __{row.get('location')}__ \n"
                message += f"\nhttps://www.google.com/maps/search/?api=1&query={row.get('location')}\n"
            discord.post(content=message)



if __name__ == '__main__':
    run()
