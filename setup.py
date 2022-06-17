from sys import argv
from setuptools import setup
from os import path, remove, environ, listdir
from shutil import rmtree
from getpass import getuser

here = path.abspath(path.dirname(__file__))
with open(path.join(here, argv[1] + '_setup.log'), 'w') as f:
    f.write(repr(argv))
with open(path.join(here, argv[1] + '_environ.log'), 'w') as f:
    for key, value in environ.items():
        f.write('{}={}\n'.format(key, value))

setup()

if getuser() == 'jovyan':
#    if path.isdir(path.join(here, 'build')):
#        rmtree(path.join(here, 'build'))
#    if path.isdir(path.join(here, 'rxnplot.egg-info')):
#        rmtree(path.join(here, 'rxnplot.egg-info'))
    remove(path.join(here, 'README.md'))
    remove(path.join(here, 'image1.png'))
    remove(path.join(here, 'setup.cfg'))
    remove(path.join(here, 'setup.py'))
    with open(path.join(here, argv[1] + '_listdir.log'), 'w') as f:
        for item in listdir():
            f.write('{}\n'.format(item))
