#! /usr/local/bin
# -*- coding: utf-8 -*-

#    rxnlvl 0.21
#    Copyright (C) 2014  Richard Terrett
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .rxnlvl_util import validateColour
from .energy import unit_prettyprint

class baseline():
    def __init__(self, colour=0x0, mode='dashed', opacity=0.5):
        # Ensure colour is a 24 bit hex colour.
        if validateColour(colour):
            self.colour = colour
        else:
            sys.stderr.write('{0} has invalid colour: {1}\n'.format(
            self.describeLevel(name),
            colour
            ))
            sys.exit(1)
        try:
            assert opacity >= 0.0 and opacity <= 1.0, 'Invalid opacity on edge {0} to {1}: {2}\n'.format(
            self.start,
            self.end,
            '{0}%'.format(opacity*100.0) if type(opacity) in [int, float] else opacity
            )
        except AssertionError as e:
            sys.stderr.write(str(e))
            sys.exit(1)
        self.opacity = opacity
        self.mode    = mode
    def getQualifiedEnergy(self, units, digits):
        # Gets pretty-printed energy - used for qualified annotation only
        return('{{:.{}f}} {{}}'.format(digits).format(0.0, unit_prettyprint[units]))
    def getUnqualifiedEnergy(self, units, digits):
        return('{{:.{}f}}'.format(digits).format(0.0))
    def getVisualHeight(self):
        return(self.__visual_height)
    def setVisualHeight(self, energyRange, zero):
        # Internal setter for the visual y-pos of the baseline, expressed as a percentage coordinate on the canvas
        self.__visual_height = 100.0-(((zero-energyRange[0])/(energyRange[1]-energyRange[0]))*100.0)
    def getVisualLeft(self):
        return(0.0)
    def getVisualRight(self):
        return(100.0)
    def getColour(self):
        return(self.colour)
    def getMode(self):
        if self.mode in ['normal',  'solid',    'continuous',      '']: return('')
        if self.mode in [  'dash', 'dashed', 'discontinuous','broken']: return('stroke-dasharray="5,5"')
    def getOpacity(self):
        return(self.opacity)
