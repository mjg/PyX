#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
from pyx import *

r = canvas.canvas()
r.stroke(path.line(0, 0, 0.15, 0.15))
r.writeEPSfile("epsbbox-inc", bboxenlarge=0)

s = canvas.canvas()
s.insert(r, [trafo.scale(10)])
elow = epsfile.epsfile(0, 0, "epsbbox-inc.eps", scale=10)
ehigh = epsfile.epsfile(0, 0, "epsbbox-inc.eps", scale=10, hiresbbox=1)

c = canvas.canvas()
x = 0

for cc in [s, elow, ehigh]:
  c.stroke(cc.bbox().rect(), [color.rgb.red, trafo.translate(x,0)])
  c.insert(cc, [trafo.translate(x,0)])
  x += cc.bbox().width()*1.2

c.writeEPSfile("epsbbox")
c.writePDFfile("epsbbox")
