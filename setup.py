from sys import argv
from setuptools import setup
from os import path, remove
from shutil import rmtree
from re import fullmatch

setup()

try:
    if argv[2] == '-d' and fullmatch('/tmp/pip-wheel-[a-z0-9]{8}', argv[3]):
        here = path.abspath(path.dirname(__file__))
        rmtree(path.join(here, 'build'))
        rmtree(path.join(here, 'rxnplot.egg-info'))
        remove(path.join(here, 'README.md'))
        remove(path.join(here, 'image1.png'))
        remove(path.join(here, 'setup.cfg'))
        remove(path.join(here, 'setup.py'))
except IndexError:
    pass
