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




def loading():
    """ hide loading id and show
    container-1  """
    doc['container-1'].style.display = "block"
    doc['loading'].style.display = "none"


win.onload = loading()