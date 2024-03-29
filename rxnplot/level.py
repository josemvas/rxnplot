#! /usr/bin/python
# -*- coding:utf-8 -*-

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
from .energy import unit_conversion, unit_prettyprint

class level:
   # energy        = None # energy(float/int, string)
   # name          = None # string
   # location      = 0    # int, >= 1
   # color         = 'black' # string
   # visual_left   = None # float, internal
   # visual_right  = None # float, internal
   # visual_height = None # float, internal

    def __init__(self, energy, location, name=None, color='black'):
        # Validation of energy is done inside energy class
        self.energy = energy
        # Validate location. Locations must be positive nonzero integers. Locations should start at 1 and be contiguous.
#        try:
#            assert type(location) == int, '{0} does not have an integer location.\n'.format(
#            self.describeLevel(name)
#            )
#        except AssertionError as e:
#            sys.stderr.write(e)
#            sys.exit(1)
        try:
            assert location > 0, 'supplied location ({0}) of {1} must be greater than 0.\n'.format(
            str(self.location),
            self.describeLevel(name)
            )
        except AssertionError as e:
            sys.stderr.write(str(e))
            sys.exit(1)
        self.location = location
        # Locations don't require names but not supplying one makes it really hard to connect.
        self.name = name
        self.color = color
        # Ensure color is a valid SVG color.
        if validateColour(color):
            self.color = color
        else:
            sys.stderr.write('{0} has invalid color: {1}\n'.format(
            self.describeLevel(name),
            color
            ))
            sys.exit(1)

    def __repr__(self):
        # For debugging and rebugging
        return('<level {0} at {1}, location: {2}, color: {3}>\n'.format(
        self.describeLevel(self.name),
        str(self.energy),
        str(self.location),
        hex(self.color))
        )

    def getEnergy(self):
        # Requests raw numeric energy in kJ/mol - used for positioning and unqualified annotation
        return(self.energy.energy)

    def getQualifiedEnergy(self, zero, units, decimals):
        # Gets pretty-printed energy - used for qualified annotation only
        return('{{:.{}f}} {{}}'.format(decimals).format((self.energy.energy - zero)/unit_conversion[units], unit_prettyprint[units]))

    def getUnqualifiedEnergy(self, zero, units, decimals):
        return('{{:.{}f}}'.format(decimals).format((self.energy.energy - zero)/unit_conversion[units]))

    def getLocation(self):
        # The ordinal position of the level
        return(self.location)

    def getColour(self):
        # The color of the level
        return(self.color)

    def getName(self):
        # The external name of the level
        return(self.name)

    def describeLevel(self, name):
        # A descriptor of the level of the purpose of debugging, which can deal with nameless levels
        if (name == None):
            return('untitled level')
        else:
            return('level {0}'.format(name))

    def setVisualHeight(self, energyRange):
        # Internal setter for the visual y-pos of the level, expressed as a percentage coordinate on the canvas
        self.visual_height = 100.0-(((self.getEnergy()-energyRange[0])/(energyRange[1]-energyRange[0]))*100.0)

    def getVisualHeight(self):
        # Getter for the visual y-pos of the level, expressed as a percentage coordinate on the canvas
        return(self.visual_height)

    def setVisualLeft(self, sliceWidth, hbuf):
        # Internal setter for the visual x-pos of the left hand side of the level, expressed as a percentage coordinate on the canvas
        self.visual_left = float(self.location-1)*(sliceWidth*2)+(hbuf/2)

    def getVisualLeft(self):
        # Getter for the visual x-pos of the left hand side of the level, expressed as a percentage coordinate on the canvas
        return(self.visual_left)

    def setVisualRight(self, sliceWidth, hbuf):
        # Internal setter for the visual x-pos of the right hand side of the level, expressed as a percentage coordinate on the canvas
        self.visual_right = (float(self.location-1)*(sliceWidth*2)+sliceWidth)+(hbuf/2)

    def getVisualRight(self):
        # Getter for the visual x-pos of the right hand side of the level, expressed as a percentage coordinate on the canvas
        return(self.visual_right)
