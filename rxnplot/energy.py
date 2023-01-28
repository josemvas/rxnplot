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

unit_conversion = { 'kjmol':        1.0,
                    'eh':        2625.5,
                    'ev':          96.487,
                    'kcalmol':         4.184,
                    'wavenumber':   0.011963
                  }

unit_prettyprint = { 'kjmol':     'kJ/mol',
                     'eh'   :     'Hartree',
                     'ev'   :     'eV',
                     'kcalmol' :     'kcal/mol',
                     'wavenumber':'cm⁻¹'
                   }

class energy:
    #units = ''
    #factor_conversion = 0.0
    #energy = 0.0
    def __init__(self,energy,units,name=None):
        try:
            assert units in unit_conversion.keys(), 'Unrecognised unit: {0}'.format(
            str(units)
            )
        except AssertionError as e:
            sys.stderr.write(e)
            sys.exit(0)
        try:
            self.energy = float(energy)*unit_conversion[units]
        except ValueError as e:
            sys.stderr.write('Could not interpret energy: {0} {1}'.format(
            str(energy),
            unit_prettyprint[units]
            ))
            sys.exit(1)
