from browser import document as doc, window as win
from browser.template import Template

Template(doc['container-1']).render(greeting="Hello", name="World")
Template(doc['container-2']).render(greeting="你好", name="世界")


def loading():
    """ hide loading id and show
    container-1 and container-2 """
    doc['container-1'].style.display = "block"
    doc['container-2'].style.display = "block"
    doc['loading'].style.display = "none"


win.onload = loading()
