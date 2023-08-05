#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Date: 
    Thu Jun 13 10:47 2019
Author: 
    Olivier Stocker 
    NanBlanc
Project: 
    OSToolBox    
"""

from setuptools import setup

setup(name='OSToolBox',
      version='1.2',
      description='implement many basic function as tools for GIS coding',
      url='https://github.com/NanBlanc/OSToolBox',
      author='Olivier Stocker',
      author_email='stocker.olivier@gmail.com',
      license='MIT',
      install_requires=['numpy','matplotlib'],
      packages=['OSToolBox','GDALToolBox'],
      zip_safe=False)