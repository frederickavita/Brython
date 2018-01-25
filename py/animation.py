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


animation = {'fade': fade(),
             'opacity': opacity(),
             'top': animatetop(),
             'left': animateleft(),
             'right': animateright(),
             'bottom': animatebottom(),
             'zoom': animatezoom()}


def sheet(x, dom_type, type_animation):
    if type_animation in animation:
        shee = doc.createElement('style')
        if dom_type == 'id':
            shee.innerHTML = "#" + x + animation[type_animation]
            doc[x].appendChild(shee)
        elif dom_type == 'class':
            shee.innerHTML = "." + x + animation[type_animation]
            doc.body.appendChild(shee)
    else:
        print('module object has no attribute ' + type_animation)


def search_div():
    data_animation = doc.querySelectorAll('[data-animation]')
    if len(data_animation) != 0:
        for data in data_animation:
            if data.id:
                sheet(data.id, 'id', data.dataset.animation)
            elif data.className:
                list_className = data.className.split()
                sheet(list_className[0], 'class', data.dataset.animation)
            else:
                format_attribut = '{div}[data-animation*={anim}]'.format(div=data.localName,
                                                                     anim=data.dataset.animation)
                s = doc.querySelectorAll(format_attribut)
                for x in s:
                    if x.className == '':
                        x.className = "brython-animation"
                        sheet(x.className, 'class', data.dataset.animation)



search_div()
