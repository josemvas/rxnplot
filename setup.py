from sys import argv
from setuptools import setup
from shutil import rmtree
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'setup.log'), 'w') as f:
    f.write(repr(argv))

setup()

if 'install' in argv:
    rmtree(path.join(here, 'build'))
    rmtree(path.join(here, 'rxnplot.egg-info'))
