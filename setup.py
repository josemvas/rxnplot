from sys import argv
from setuptools import setup
from shutil import rmtree
setup()
if 'install' in argv:
    rmtree('build')
    rmtree('rxnplot.egg-info')
