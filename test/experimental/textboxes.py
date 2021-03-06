import sys; sys.path[:0] = ["../.."]
import random, string
from pyx import *

text.set(texipc=1)
text.set(mode="tex", texdebug="debug.tex", usefiles=["debug.dvi", "debug.log"])

def randpar():
    return " ".join(["".join([random.choice(string.lowercase)
                              for j in range(random.randint(1, 3))])
                     for i in range(random.randint(100, 300))])

def randparwithdisplay():
    #par = "" # TODO allow for formulas at the beginning -- to be checked
    par = randpar()
    for i in range(random.randint(0, 3)):
        par += r"\display{}xxx\enddisplay{}"
        for j in range(random.randint(0, 1)):
            par += randpar()
    #return par # TODO allow for formulas at the end -- to be checked
    return par + randpar()

def randtext():
    return r"\par{}".join([randparwithdisplay() for i in range(random.randint(1, 10))])

def output(boxes, shapes):
    c = canvas.canvas()
    y = 0
    tr = text.texrunner()
    for i in range(len(boxes)):
        if i < len(shapes):
            shape = shapes[i]
        c.stroke(path.rect(0, y, shape[0], -shape[1]))
        c.stroke(boxes[i].bbox().path(), [trafo.translate(0, y), color.rgb.red])
        c.insert(boxes[i], [trafo.translate(0, y)])
        for mark in list(boxes[i].markers.keys()):
            mx, my = boxes[i].markers[mark]
            c.insert(tr.text(mx,my+y, mark+"~", [text.size.tiny, text.halign.right]))
            if mark[:5] == "start":
                c.fill(path.circle(mx, my+y, 0.05), [color.rgb.red])
            elif mark[:3] == "end":
                c.fill(path.circle(mx, my+y, 0.05), [color.rgb.green])
            else:
                raise ValueError("other marks in there!")
        y -= shape[1] + 3
    c.writeEPSfile("textboxes")

random.seed(0)
shapes = [(10,7), (8,5)]*50
n = 0
only = 28
while only is None or n <= only:
    print(n)
    n += 1
    if 1:
        thistext = randtext()
        thistextfile = open("debug.thistext", "w")
        thistextfile.write(thistext)
        thistextfile.close()
    else:
        thistextfile = open("debug.thistext", "r")
        thistext = thistextfile.read()
        thistextfile.close()
    if only is not None and n <= only:
        continue
    boxes = text.defaulttexrunner.textboxes(thistext, shapes)
    output(boxes, shapes)
    for i in range(len(boxes)):
        if i < len(shapes):
            shape = shapes[i]
        if abs(unit.topt(boxes[i].bbox().right()) - unit.topt(shape[0])) > 1:
            print(("right boundary differs:",
                   unit.topt(boxes[i].bbox().bottom()), -unit.topt(shape[1]),
                   unit.topt(boxes[i].bbox().right()), unit.topt(shape[0]),
                   i+1, len(boxes)))

