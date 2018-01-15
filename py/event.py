from browser import document as doc, window as win, alert
from browser.template import Template



def func_activate(ev, elt):
    alert("Activate")


Template(doc["container-1"], [func_activate]).render(activate="activate")

number = 0


def incr(ev, elt):
    elt.data.number += 1


def decr(ev, elt):
    elt.data.number -= 1


def incre(ev, elt):
    elt.data.number_2 += 1


def decre(ev, elt):
    elt.data.number_2 -= 1


def rest(ev, elt):
    elt.data.number = 0


def reste(ev, elt):
    elt.data.number_2 = 0


Template(doc["container-2"], [incr, decr]).render(number=number)

Template(doc["container-3"], [incr, decr, incre, decre, rest, reste]).render(number=number, number_2=number)

listener = True


def activiate(ev, elt):
    if listener:
        alert("Activating!")


def deactivate(ev, elt):
    if listener:
        alert("Deactivating!")


def toogle(ev, elt):
    if elt.data.silence == "Silence":
        elt.data.silence = "Resume"
    elif elt.data.silence == "Resume":
        elt.data.silence = "Silence"


def stop(ev, elt):
    global listener
    listener = False
    alert("No more alerts!")


Template(doc["container-4"], [activiate, deactivate, toogle, stop]).render(silence="Silence")


def prompt(ev, elt):
    name = win.prompt('Enter your username to sign in', 'ractive_fan')
    if len(name) == 0:
        name = "Guest star"
    doc['signed'].style.display = "block"
    doc['nosigned'].style.display = "none"
    doc['username'].text = name.title()


username = None
non_1 = "none"
non_2 = 'block'

Template(doc["container-5"], [prompt]).render(username=username, non_1=non_1, non_2=non_2)


def loading():
    """ hide loading id  """
    doc['loading'].style.display = "none"
    doc["opacity"].style.opacity = "1"


win.onload = loading()



