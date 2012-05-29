from pyx import *

c = canvas.canvas()

cd = canvas.canvas()

cd.stroke(path.line(0,0,1,0), [deco.earrow])
cd.stroke(path.line(0,0,0,1), [deco.earrow])
cd.stroke(path.path(path.moveto(0.8,0), path.arc(0,0,0.6,0,90)),
    [deco.earrow, style.linestyle.dotted])

c.insert(cd, [trafo.translate(0,1)])
c.stroke(path.curve(2,2, 6,0, 0,0, 4,2),
    [deco.insert(cd, [trafo.scale(0.6)], relarclenpos=p, relangle=0) for p in [0, 0.3, 0.5, 0.7, 1]])

c.writeEPSfile()
c.writePDFfile()
