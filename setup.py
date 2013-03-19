#!/usr/bin/env python
from setuptools import setup, find_packages

packages=find_packages()

setup(
    name = "pwgen",
    version = "0.4",
    description = "Pure python version of pwgen",
    long_description = "Simple version of pwgen to generate random password or strings",
    author = "Vince Spicer",
    author_email = "vinces1979@gmail.com",
    url = "https://github.com/vinces1979/pwgen",
    license = "MIT",
    platforms = ["any"],
    packages=packages,
    keywords = [
        'pwgen', 'password', 'strings', 'random'
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
