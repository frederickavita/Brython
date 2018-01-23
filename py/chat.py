from browser import document as doc, window as win, html
from browser.local_storage import storage
import json
chat = []
user = False
chat_rec = ''
check = False

def checking_chat():
    global chat_rec
    global chat
    global check
    if "chat" not in storage:
        return False
    else:
        if check is False:
            chat_rec = storage['chat']
            chat_rec = json.loads(chat_rec)
            chat = chat_rec
            for x in chat_rec:
                doc['controle'] <= html.B(x[0]) + " : " + x[1] + html.BR()
            check = True



checking_chat()




def input(ev):
    global user
    global chat
    global check
    global  chat_rec
    if user:
        name = user
    else:
        name = 'Anonnymous'
    if checking_chat() is False and check is False:
        check = True
        if ev.target.value != '':
            print("bvbvbvbvv")
            text_chat = [name, ev.target.value, win.Date.now()]
            chat.append(text_chat)
            chat_rec = json.dumps(chat)
            storage['chat'] = chat_rec
            doc['controle'] <= html.B(name) + " : " + ev.target.value + html.BR()
            ev.target.value = ""
    else:
        if ev.target.value != '':
            doc['controle'] <= html.B(name) + " : " + ev.target.value + html.BR()
            print("zeazeazea")
            text_chat = [name, ev.target.value, win.Date.now()]
            ev.target.value = ""
            chat.append(text_chat)
            chat_rec = json.dumps(chat)
            storage['chat'] = chat_rec





doc['message'].bind("change", input)


def loading():
    doc['loading'].style.display = "none"
    doc['container'].style.display = "block"




doc['welcome'].text = "Chatapp"



win.load = loading()
