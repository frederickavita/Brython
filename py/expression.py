from browser import document as doc, window as win
from browser.template import Template
import math


def country(country, population):
    return {'country': country, 'population': population}


millnames = ['', ' Thousand', ' Million', ' Billion', ' Trillion']


def format(n):
    n = float(n)
    millidx = max(0, min(len(millnames) - 1,
                         int(math.floor(0 if n == 0 else math.log10(abs(n)) / 3))))

    return '{:.0f}{}'.format(n / 10 ** (3 * millidx), millnames[millidx])


b = country(country="The UK", population=format(63230000))

appl_tmpl = Template(doc["container-1"])
appl_tmpl.render(country=b['country'], population=b['population'])


def country(name, climate, population, capital):
    return {'name': name, 'climate': climate,
            'population': population, 'capital': capital}


b = country(name="The UK", climate={'temperature': 'cold', 'rainfall': 'excess'}, population=63230000,
            capital={'name': 'London', "lat": 51.5171, 'lon': -0.1062})

appl_tmpl = Template(doc["container-2"])

appl_tmpl.render(country_name=b['name'],
                 country_climate_temperature=b['climate']['temperature'],
                 country_climate_rainfall=b['climate']['rainfall'],
                 country_population=b['population'],
                 country_capital_name=b['capital']['name'],
                 country_capital_lat=b['capital']['lat'],
                 country_capital_lon=b['capital']['lon'])


def loading():
    """ hide loading id and show
    container-1  """
    doc['container-1'].style.display = "block"
    doc['container-2'].style.display = "block"
    doc['loading'].style.display = "none"


win.onload = loading()
