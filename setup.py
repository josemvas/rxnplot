from sys import argv
from getpass import getuser
from setuptools import setup
from os import path, remove
from shutil import rmtree

setup()

if getuser() == 'jovyan' and argv[1] == 'bdist_wheel':
    here = path.abspath(path.dirname(__file__))
    remove(path.join(here, 'LICENSE'))
    remove(path.join(here, 'README.md'))
    remove(path.join(here, 'image1.png'))
    remove(path.join(here, 'setup.cfg'))
    remove(path.join(here, 'setup.py'))
    rmtree(path.join(here, 'build'))
    rmtree(path.join(here, 'rxnplot'))
    rmtree(path.join(here, 'rxnplot.egg-info'))
