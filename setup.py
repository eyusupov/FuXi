#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
try:
    import multiprocessing  # atexit exception
except:
    pass


config = dict(
    name="FuXi",
    version="1.4",
    description="An OWL / N3-based in-memory, logic reasoning system for RDF",
    author="Chime Ogbuji",
    author_email="chimezie@gmail.com",
    maintainer="RDFLib Team",
    maintainer_email="rdflib-dev@google.com",
    platforms=["any"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
       ],
    package_dir={
        'FuXi': 'lib',
    },
    packages=[
        "FuXi",
        "FuXi.LP",
        "FuXi.SPARQL",
        "FuXi.Rete",
        "FuXi.DLP",
        "FuXi.Horn",
    ],
    install_requires=['rdflib>2'],
    license="Apache",
    keywords="python logic owl rdf dlp n3 rule reasoner",
    test_suite='nose.collector',
    url="https://github.com/RDFLib/FuXi",
    entry_points={
        'console_scripts': [
           'FuXi = FuXi.Rete.CommandLine:main',
        ],
    },
    zip_safe=False
)

kwargs = {}
try:
    from setuptools import setup
    assert setup
except ImportError:
    from distutils.core import setup

setup(**config)
