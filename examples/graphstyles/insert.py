from pyx import *

class insertstyle(graph.style.symbol):
    """a graph style which calls a translate_pt method of the symbol to insert
    the result instead of calling the symbol to get a path to be drawn"""

    def selectstyle(self, privatedata, sharedata, graph, selectindex, selecttotal):
        privatedata.symbol = attr.selectattr(self.symbol, selectindex, selecttotal)
        privatedata.size_pt = unit.topt(attr.selectattr(self.size, selectindex, selecttotal))
        privatedata.insertcanvas = canvas.translateablecanvas()
        if self.symbolattrs is not None:
            privatedata.symbolattrs = attr.selectattrs(self.defaultsymbolattrs + self.symbolattrs, selectindex, selecttotal)
        else:
            privatedata.symbolattrs = None
        # stroke symbol on insertcanvas instead of symbolcanvas
        privatedata.symbol(privatedata.insertcanvas, 0, 0, privatedata.size_pt, privatedata.symbolattrs)

    def drawpoint(self, privatedata, sharedata, graph, point):
        if sharedata.vposvalid and privatedata.symbolattrs is not None:
            x_pt, y_pt = graph.vpos_pt(*sharedata.vpos)
            # use more efficient version of privatedata.symbolcanvas.insert(privatedata.insertcanvas,[trafo.translate_pt(x_pt, y_pt)])
            privatedata.symbolcanvas.insert(privatedata.insertcanvas.translate_pt(x_pt, y_pt))

    # key_pt is inherited from graph.style.symbol because reimplementing would save only one instance


 
g = graph.graphxy(width=8)
g.plot(graph.data.function("y(x)=x*x", min=-1, max=1, points=1000),
#       [graph.style.symbol(graph.style.symbol.circle, symbolattrs=[deco.filled,color.rgb.blue, deco.stroked.clear])])
       [insertstyle(graph.style.symbol.circle, symbolattrs=[deco.filled,color.rgb.blue, deco.stroked.clear])])
g.writeEPSfile("insert")
