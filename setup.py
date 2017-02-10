#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@date: 2016-04-14

@author: Devin
"""
from setuptools import setup, find_packages
setup(name='commlib',
    version='1.0.11',
    packages = find_packages(),
    description='common tools for develop',
    author='Devin',
    author_email='waipbmtd@gmail.com',
    url='https://github.com/waipbmtd/commlib',
    license='GPL',
    install_requires=[
        'python-dateutil',
        'python-memcached',
        'redis',
        'Fabric',
        'Jinja2',
      ],
    )