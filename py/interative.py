from browser import document as doc, window as win
from browser.template import Template

xmens = [{'name': 'Nightcrawler',
          'realname': 'Wagner, Kurt',
          'power': 'Teleportation',
          'info': 'http://www.superherodb.com/Nightcrawler/10-107/'},
         {'name': 'Cyclops',
          'realname': 'Summers, Scott',
          'power': 'Optic blast',
          'info': 'http://www.superherodb.com/Cyclops/10-50/'},
         {'name': 'Rogue',
          'realname': 'Marie, Anna',
          'power': 'Absorbing powers',
          'info': 'http://www.superherodb.com/Rogue/10-831/'},
         {'name': 'Wolverine',
          'realname': 'Howlett, James',
          'power': 'Regeneration',
          'info': 'http://www.superherodb.com/Wolverine/10-161/'}]

Template(doc["container-1"]).render(xmens=xmens,
                                    name="name",
                                    realname="realname",
                                    power="power",
                                    position=0)


def loading():
    """ hide loading id and show
    container-1 """
    doc['container-1'].style.display = "block"
    doc['loading'].style.display = "none"


win.onload = loading()
