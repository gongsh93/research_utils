# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os 

def read_version():
    version_file = os.path.join('research_utils', 'version.py')
    with open(version_file, 'r') as f:
        exec(f.read(), globals())
        return globals()['__version__']

setup(
    name='research_utils', 
    version=read_version(),
    packages=find_packages(),
    description='Utility functions for research projects',
    author="Seonghyeon Gong",
    author_email='gongsh93@gmail.com',
    keywords=['data', 'research', 'preprocessing'],
    install_requires=[
        # Dependencies 
        'pandas>=2.0.0',
    ],
)