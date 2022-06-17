from sys import argv
from setuptools import setup
from os import path, remove, environ
from shutil import rmtree
from re import fullmatch

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'setup.log'), 'w') as f:
    f.write(repr(argv))
    f.write(environ.get('BINDER_LAUNCH_HOST', 'UNSET'))

setup()

try:
    if argv[2] == '-d' and fullmatch('/tmp/pip-wheel-[a-z0-9]{8}', argv[3]):
        rmtree(path.join(here, 'build'))
        rmtree(path.join(here, 'rxnplot.egg-info'))
        remove(path.join(here, 'README.md'))
        remove(path.join(here, 'image1.png'))
        remove(path.join(here, 'setup.cfg'))
        remove(path.join(here, 'setup.py'))
        with open(path.join(here, 'remove.log'), 'w') as f:
            f.write('sucess')
except IndexError:
    pass
