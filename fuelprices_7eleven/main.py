import click
from tabulate import tabulate

from seven11fuelprices.price_lookup import LookupPrices
from discordwebhook import Discord

@click.command()
@click.option('-t','--top',default=3, type=int)
def cheep(top):
    lookupPrices = LookupPrices()
    lookupPrices.get_top(top)
    for type, data in lookupPrices.items:
        if len(data) > 0:
            print(type)
            print(tabulate(data,headers="keys",tablefmt="rounded_grid"))
            print(" ")

def prices():
    lookupPrices = LookupPrices()



if __name__ == '__main__':
    cheep()
