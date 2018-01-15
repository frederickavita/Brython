from browser import document as doc, window as win
from browser.template import Template
import random


product = [["pint of milk", 0.19, 7],
           ['banane', 0.78, 3],
           ['orange', 0.25, 2],
           ['juice', 0.60, 1]]

item = product[0][0]
price = product[0][1]
quantity = product[0][2]


def formate(num, quant):
    """
    change format
    according to the result
    """
    num = num * quant
    if num < 1:
        num = 100 * num
        return '{0}p'.format(str(num))
    else:
        num = round(num, 2)
        return '£{0}'.format(str(num))


app_tmpl = Template(doc["container-1"])
app_tmpl.render(item=item, price=price,
                quantity=quantity,
                total=formate(price, quantity))


def update_value(ev, elt):
    global product
    """
    update new value
    """
    prod = random.choice(product)
    app_tmpl.render(item=prod[0],
                    price=prod[1],
                    quantity=prod[2],
                    total=formate(prod[1], prod[2]))
    doc['container-1'].style.display = "block"
    doc['container-2'].style.display = "block"""


Template(doc["container-2"], [update_value]).render(item=item,
                                                    price=price,
                                                    quantity=quantity,
                                                    update="update random",
                                                    total=formate(price, quantity))


def loading():
    """ hide loading id and show
    container-1 and container-2 """
    doc['container-1'].style.display = "block"
    doc['container-2'].style.display = "block"
    doc['loading'].style.display = "none"


win.onload = loading()
