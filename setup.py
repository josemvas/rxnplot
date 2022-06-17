from setuptools import setup
from os import path, environ, remove
from shutil import rmtree

setup()

if 'BINDER_SERVICE_HOST' in os.environ:
    here = path.abspath(path.dirname(__file__))
    rmtree(path.join(here, 'build'))
    rmtree(path.join(here, 'rxnplot.egg-info'))
    remove(path.join(here, 'image1.png')
    remove(path.join(here, 'setup.cfg')
    remove(path.join(here, 'setup.py')
