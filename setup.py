#! /usr/bin/env python
#
# Copyright (C) 2021 Mikko Kotila

DESCRIPTION = "A Python wrapper for the BDRC API to access meta-data on Tibetan texts."
LONG_DESCRIPTION = """\
"""

DISTNAME = 'BDRC'
MAINTAINER = 'Mikko Kotila'
MAINTAINER_EMAIL = 'mailme@mikkokotila.com'
URL = 'https://github.com/Lotus-King-Trust/BDRC'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/Lotus-King-Trust/BDRC'
VERSION = '0.1'

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

install_requires = ['pandas',
                    'numpy',
                    'wrangle',
                    'tqdm',
                    'rdflib']


if __name__ == "__main__":

    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          packages=['bdrc',
                    'bdrc.methods',
                    'bdrc.namespaces',
                    'bdrc.utils',
                    'bdrc.workflows'],

          classifiers=['Intended Audience :: Science/Research',
                       'Programming Language :: Python :: 3.8',
                       'License :: OSI Approved :: MIT License',
                       'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                       'Operating System :: POSIX',
                       'Operating System :: Unix',
                       'Operating System :: MacOS',
                       'Operating System :: Microsoft :: Windows :: Windows 10'])