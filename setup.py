from setuptools import setup
from socket import gethostname
from os import path, environ, remove
from shutil import rmtree
import sys

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'setup.log'), 'w') as f:
    f.write(repr(sys.argv))

setup()

#if gethostname().startswith('jupyter-'):
#    rmtree(path.join(here, 'build'))
#    rmtree(path.join(here, 'rxnplot.egg-info'))
#    remove(path.join(here, 'README.md'))
#    remove(path.join(here, 'image1.png'))
#    remove(path.join(here, 'setup.cfg'))
#    remove(path.join(here, 'setup.py'))
