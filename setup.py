import setuptools

#min_stversion = '30.3' # Minimum Setuptools version supporting configuration metadata in setup.cfg
min_stversion = '32.2' # Minimum Setuptools version supporting conditional python dependencies (PEP 508)

# Setup package if Setuptools version is high enough
setuptools.setup(setup_requires=['setuptools>=' + min_stversion])

