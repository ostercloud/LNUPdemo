# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import LNUPdemo
version = LNUPdemo.__version__

setup(
    name='LNUPdemo',
    version=version,
    author='',
    author_email='allen.oster@rackspace.com',
    packages=[
        'LNUPdemo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['LNUPdemo/manage.py'],
)