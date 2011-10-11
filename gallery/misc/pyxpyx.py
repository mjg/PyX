from pyx import *
from pyx.dvi.mapfile import MAPline

f = MAPline('cmb10 CMB10 <cmb10.pfb').getfont()

c = canvas.canvas()
tpath = f.text(0, 0, "PyX", 300).textpath().reversed()
t = r"\PyX is fun. "
n = int(tpath.arclen() / text.text(0, 0, t).width)
c.draw(tpath, [deco.curvedtext(t*n)])

c.writeEPSfile("pyxpyx")
c.writePDFfile("pyxpyx")
