#! /usr/bin/python
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

import sys
from .rxnlvl_util import validateColour

class edge:
    # start   = None     # string
    # end     = None     # string
    # color   = 'black'  # string
    # opacity = 1.0      # float, 0.0:1.0
    # mode    = 'normal' # string
    
    def __init__(self, start, end, color='black', opacity=1.0, mode='normal'):
        try:
            assert start != end, 'Degenerate edge detected in input: {0} to {1}\n'.format(start, end)
        except AssertionError as e:
            sys.stderr.write(str(e))
            sys.exit(1)
        self.start   = start
        self.end     = end
        # Ensure color is a valid SVG color.
        if validateColour(color):
            self.color = color
        else:
            sys.stderr.write('{0} has invalid color: {1}\n'.format(
            self.describeLevel(name),
            color
            ))
            sys.exit(1)
        # Make sure edge opacity is a number between 0.0 and 1.0
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

    def __repr__(self):
        return('<edge from {0} to {1}, color: {2}, opacity: {3}, mode: {4}>'.format(
        self.start,
        self.end,
        hex(self.color),
        str('{0}%'.format(self.opacity*100)),
        self.mode))

    def getStart(self):
        return(self.start)

    def getEnd(self):
        return(self.end)

    def getColour(self):
        return(self.color)

    def getMode(self):
        if self.mode in ['normal',  'solid',    'continuous',      '']: return('')
        if self.mode in [  'dash', 'dashed', 'discontinuous','broken']: return('stroke-dasharray="5,5"')

    def getOpacity(self):
        return(self.opacity)
