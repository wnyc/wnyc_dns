#!/usr/bin/env python

"""
WNYC_DNS
=================
Simple tools used at WNYC to manage DNS entries
"""

from setuptools import setup

setup(
    name='wnyc_dns',
    version='0.0.1',
    author='Adam DePrince',
    author_email='adeprince@nypublicradio.org',
    description='Tools to help you leave rackspace',
    url="",
    long_description=__doc__,
    py_modules=[
        'wnyc_dns/__init__',
        'wnyc_dns/rackspace',
        'wnyc_dns/common',
        ],
    packages=['wnyc_dns',],
    zip_safe=True,
    license='GPLv3',
    include_package_data=True,
    classifiers=[],
    scripts=['scripts/wnyc_dns'],
    install_requires=[
        'python-clouddns',
        'gevent',
        'python-gflags',
        ]
    )
