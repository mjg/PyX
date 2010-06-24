#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
#
#
# Copyright (C) 2002-2004 J�rg Lehmann <joergl@users.sourceforge.net>
# Copyright (C) 2003-2004 Michael Schindler <m-schindler@users.sourceforge.net>
# Copyright (C) 2002-2004 Andr� Wobst <wobsta@users.sourceforge.net>
#
# This file is part of PyX (http://pyx.sourceforge.net/).
#
# PyX is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PyX is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyX; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA


from pyx import box, canvas, text, unit


class key:

    defaulttextattrs = [text.vshift.mathaxis]

    def __init__(self, dist=0.2*unit.v_cm, pos="tr", hpos=None, vpos=None,
                 hinside=1, vinside=1, hdist=0.6*unit.v_cm, vdist=0.4*unit.v_cm,
                 symbolwidth=0.5*unit.v_cm, symbolheight=0.25*unit.v_cm, symbolspace=0.2*unit.v_cm,
                 textattrs=[], border=0.3*unit.v_cm, keyattrs=None):
        self.dist = dist
        self.hinside = hinside
        self.vinside = vinside
        self.hdist = hdist
        self.vdist = vdist
        self.symbolwidth = symbolwidth
        self.symbolheight = symbolheight
        self.symbolspace = symbolspace
        self.textattrs = textattrs
        self.border = border
        self.keyattrs = keyattrs
        if pos is not None:
            if vpos is not None or hpos is not None:
                raise ValueError("either specify pos or a combination of hpos, vpos")
            for poslist, hpos, vpos in [(["tr", "rt"], 1, 1),
                                        (["tc", "ct"], 0.5, 1),
                                        (["tl", "lt"], 0, 1),
                                        (["mr", "rm"], 1, 0.5),
                                        (["mc", "cm"], 0.5, 0.5),
                                        (["ml", "lm"], 0, 0.5),
                                        (["br", "rb"], 1, 0),
                                        (["bc", "cb"], 0.5, 0),
                                        (["bl", "lb"], 0, 0)]:
                if pos in poslist:
                    self.hpos = hpos
                    self.vpos = vpos
                    break
            else:
                raise ValueError("invalid pos")
        else:
            if vpos is None or hpos is None:
                raise ValueError("either specify pos or a combination of hpos, vpos")
            self.hpos = hpos
            self.vpos = vpos

    def paint(self, plotitems):
        "creates the layout of the key"
        plotitems = [plotitem for plotitem in plotitems if plotitem.gettitle() is not None]
        c = canvas.canvas()
        self.dist_pt = unit.topt(self.dist)
        self.hdist_pt = unit.topt(self.hdist)
        self.vdist_pt = unit.topt(self.vdist)
        self.symbolwidth_pt = unit.topt(self.symbolwidth)
        self.symbolheight_pt = unit.topt(self.symbolheight)
        self.symbolspace_pt = unit.topt(self.symbolspace)
        titleboxes = []
        for plotitem in plotitems:
            titlebox = c.texrunner.text_pt(0, 0, plotitem.gettitle(), self.defaulttextattrs + self.textattrs)
            titlebox.plotitem = plotitem
            titleboxes.append(titlebox)
        dy_pt = box.tile_pt(titleboxes, self.dist_pt, 0, -1)
        box.linealignequal_pt(titleboxes, self.symbolwidth_pt + self.symbolspace_pt, 1, 0)
        y_pt = -0.5 * self.symbolheight_pt + titleboxes[0].center[1]
        for titlebox in titleboxes:
            titlebox.plotitem.key_pt(c, 0, y_pt, self.symbolwidth_pt, self.symbolheight_pt)
            y_pt -= dy_pt
        for titlebox in titleboxes:
            c.insert(titlebox)
        if self.keyattrs is not None:
            newc = canvas.canvas()
            newc.draw(c.bbox().enlarged(self.border).path(), self.keyattrs)
            newc.insert(c)
            c = newc
        return c
