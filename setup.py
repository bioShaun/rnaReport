#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.1dev'

print '''------------------------------
Installing NGS_rnaseq_report version {}
------------------------------
'''.format(version)


setup(
    name='rnareport',
    version=version,
    author='lx Gui',
    author_email='guilixuan@gmail.com',
    keywords=['bioinformatics', 'NGS', 'QC'],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/rna_report', ],
    install_requires=[
        'Jinja2',
        'configparser',
    ]

)


print '''------------------------------
NGS_rnaseq_report installation complete!
------------------------------
'''
