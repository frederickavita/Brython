from browser import document as doc, window as win
from browser.template import Template

Template(doc["container-1"]).render(red=0.45, green=0.61, blue=0.2)


def loading():
    """ hide loading id and show
    container-1 """
    doc['container-1'].style.display = "block"
    doc['loading'].style.display = "none"


win.onload = loading()
