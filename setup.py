# -*- coding: utf-8 -*-

import os

from setuptools import setup
from setuptools import find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='templer.ielectric',
    version='0.1',
    description="Collection of project templates for my personal use.",
    long_description=read('README.rst')
                     + read('HISTORY.rst')
                     + read('LICENSE'),
    classifiers=[
        "Programming Language :: Python",
    ],
    author='Domen Kožar',
    author_email='domen@dev.si',
    url='https://github.com/iElectric/templer.ielectric',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    namespace_packages=['templer'],
    install_requires=[
        'setuptools',
        'templer.core',
    ],
    extras_require={
        'test': [
            'nose',
            'scripttest',
            'unittest2',
        ]
    },
    entry_points="""
    [paste.paster_create_template]
    pyramid = templer.ielectric:Pyramid
    distribute_package = templer.ielectric:DistributePackage
    """,
)
