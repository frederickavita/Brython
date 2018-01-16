from browser import document as doc, window as win, html
from browser.template import Template

data = {}
last_key = ''
idcheck = []
bind_list = []


def create_task(event, element):
    global taskword
    if len(event.target.value) > 1:
        taskword = event.target.value


def save_task(event, element):
    global last_key
    global data
    global taskword
    if len(taskword) > 1:
        if len(data) == 0:
            last_key = 1
            data = {last_key: [taskword, False]}
            event.target.value = ''
            taskword = ''
        else:
            last_key = last_key + 1
            add_data = {last_key: [taskword, False]}
            data.update(add_data)
            event.target.value = ''
            taskword = ''


def line(event):
    id = event.target.id
    id = "m" + str(id[1:])
    if event.target.checked:
        doc[id].style.textDecoration = "line-through"
        doc[id].style.color = "grey"
    else:
        doc[id].style.textDecoration = "none"
        doc[id].style.color = "black"


def remove_item(event):
    global idcheck
    ide = event.target.id
    ide = ide[2:]
    doc["id" + str(ide)].unbind("click", remove_item)
    doc["c" + str(ide)].unbind("change", line)
    doc["m" + str(ide)].unbind("click", editing)
    doc["m" + str(ide)].unbind("blur", editing_focus)
    doc["k" + str(ide)].innerHTML = ''


styleread = {'backgound': '#ffffff', 'border-width': '2px'}
styleinput = {'background': '#f1f1f1', 'border-width': 'inherit',
              'margin-top': '5px', 'margin-left': '2px'}


def editing(event):
    id = event.target.id
    if id:
        doc[id].style.textDecoration = "none"
        doc[id].style.background = "white"
        doc[id].removeAttribute('readonly')
        doc[id].style = styleread


def editing_focus(event):
    id = event.target.id
    c = "c" + str(id[1:])
    m = "m" + str(id[1:])
    doc[id].setAttribute("readonly", "true")
    doc[id].style = styleinput
    if doc[c].checked is True:
        doc[m].style.textDecoration = "line-through"


def show_task(event, element):
    global data
    global idcheck
    global bind_list
    cla = "w3-tag w3-large w3-red"
    if len(data) != 0:
        doc['app-3'].style.display = "block"
        for x, q in data.items():
            if x not in idcheck:
                idcheck.append(x)
                span = html.SPAN("&times", id="id" + str(x), Class=cla,
                                 style={'margin-top': '4px'})

                inputcheckbox = html.INPUT(Class="w3-check w3-left", id="c" + str(x), type="checkbox")
                container = html.DIV(Class="w3-container", id="k" + str(x))
                input = html.INPUT(id="m" + str(x), Class="w3-left",
                                   value=q[0], readonly="true", style=styleinput)
                div1 = html.DIV(id=x)
                div1 <= inputcheckbox + input + span
                container <= div1
                doc['app-3'] <= container
    for x in idcheck:
        if x not in bind_list:
            bind_list.append(x)
            doc["id" + str(x)].bind("click", remove_item)
            doc["c" + str(x)].bind("change", line)
            doc["m" + str(x)].bind("click", editing)
            doc["m" + str(x)].bind("blur", editing_focus)


Template(doc["app-1"]).render(name="to-do list")

Template(doc["app-2"], [create_task, save_task, show_task]).render()

def loading():
    """ hide loading id and show
    container-1 and container-2 """
    doc["index"].style.opacity = "1"
    doc['loading'].style.display = "none"


win.onload = loading()
