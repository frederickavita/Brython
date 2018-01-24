from browser import document as doc, window as win


def fade():
    return ('{animation:fading 10s infinite}@keyframes \n'
            'fading{0%{opacity:0}50%{opacity:1}100%{opacity:0}}')


def opacity():
    return ('{animation:opac 0.8s}@keyframes \n'
            'opac{from{opacity:0} to{opacity:1}}')


def animatetop():
    return ('{position:relative;animation:animatetop 0.4s}@keyframes \n'
            'animatetop{from{top:-300px;opacity:0} to{top:0;opacity:1}}')


def animateleft():
    return ('{position:relative;animation:animatetop 0.4s}@keyframes \n'
            'animatetop{from{top:-300px;opacity:0} to{top:0;opacity:1}}')


def animateright():
    return ('{position:relative;animation:animateright 0.4s}@keyframes \n'
            'animateright{from{right:-300px;opacity:0} to{right:0;opacity:1}}')


def animatebottom():
    return ('{position:relative;animation:animatebottom 0.4s}@keyframes \n'
            'animatebottom{from{bottom:-300px;opacity:0} to{bottom:0;opacity:1}}')


def animatezoom():
    return ('{animation:animatezoom 0.6s}@keyframes \n'
            'animatezoom{from{transform:scale(0)} to{transform:scale(1)}}')


def sheet(x,dom_type):
    shee = doc.createElement('style')
    if dom_type == 'id':
        shee.innerHTML = "#" + x + animatezoom()
    doc[x].appendChild(shee)


def search_div():
    data_animation = doc.querySelectorAll('[data-animation]')
    for data in data_animation:
        if data.id:
            sheet(data.id,'id')
        elif data.classList:
            sheet(data)
    doc['container'].style.display = "block"


search_div()
