#!/usr/bin/env python

import io
import os
import re
from collections import OrderedDict

from setuptools import find_packages, setup


def get_long_description():
    for filename in ('README.rst',):
        with io.open(filename, 'r', encoding='utf-8') as f:
            yield f.read()


def get_version(package):
    with io.open(os.path.join(package, '__init__.py')) as f:
        pattern = r'^__version__ = [\'"]([^\'"]*)[\'"]'
        return re.search(pattern, f.read(), re.MULTILINE).group(1)


setup(
    name='PP6RemoteAPI',
    version=get_version('PP6RemoteAPI'),
    license='MIT',
    description='A client for the ProPresenter Remote Websocket API',
    long_description='\n\n'.join(get_long_description()),
    author='kikeh',
    author_email='heisba@gmail.com',
    maintainer='kikeh',
    url='https://github.com/kikeh/PP6RemoteAPI',
    project_urls=OrderedDict((
        ('Issues', 'https://github.com/kikeh/PP6RemoteAPI/issues'),
    )),
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'websockets==7.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    zip_safe=False,
    tests_require=[
        'websockets==7.0'
    ],
)
