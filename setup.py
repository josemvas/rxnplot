from sys import argv
from getpass import getuser
from setuptools import setup
from os import path, remove
from shutil import rmtree

setup()

if getuser() == 'jovyan' and arvg[1] == 'bdist_wheel':
    rmtree(path.join(here, 'build'))
    rmtree(path.join(here, 'rxnplot.egg-info'))
    remove(path.join(here, 'image1.png'))
    remove(path.join(here, 'README.md'))
    remove(path.join(here, 'LICENSE'))
    remove(path.join(here, 'setup.cfg'))
    remove(path.join(here, 'setup.py'))
