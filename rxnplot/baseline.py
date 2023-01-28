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

class baseline():
    def __init__(self, color='black', mode='dashed', opacity=0.5):
        # Ensure color is a valid SVG color.
        if validateColour(color):
            self.color = color
        else:
            sys.stderr.write('{0} has invalid color: {1}\n'.format(
            self.describeLevel(name),
            color
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
    def getColour(self):
        return(self.color)
    def getMode(self):
        if self.mode in ['normal',  'solid',    'continuous',      '']: return('')
        if self.mode in [  'dash', 'dashed', 'discontinuous','broken']: return('stroke-dasharray="5,5"')
    def getOpacity(self):
        return(self.opacity)
