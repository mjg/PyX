from pyx import *
 
c = canvas.canvas()

R = 1.3 
p = path.path(path.arc(0,0, R, 0,270)) + path.line(0,-R, R,-R)
label = (r"\PyX{} is fun. " * 4)[:-1] # chop off last space 

c.draw(p, [deco.stroked([color.rgb.blue]), deco.curvedtext(label)])
c.draw(p, [trafo.translate(2.5*R,0), deco.stroked([color.rgb.blue]), deco.curvedtext(label,textattrs=[text.halign.right],relarclenpos=1)])
c.draw(p.reversed(), [trafo.translate(0, -2.5*R), deco.stroked([color.rgb.blue]), deco.curvedtext(label,textattrs=[text.halign.right],relarclenpos=1)])
c.draw(p.reversed(), [trafo.translate(2.5*R, -2.5*R), deco.stroked([color.rgb.blue]), deco.curvedtext(label)])

c.writeEPSfile("textalongpath.eps")
c.writePDFfile("textalongpath.pdf")
