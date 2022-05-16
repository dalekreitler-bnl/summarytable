from setuptools import setup

setup(
    name='summarytable',
    version='0.1.0',
    author='Dale Kreitler',
    author_email='dkreitler@bnl.gov',
    packages=['summarytable',],
    scripts=['bin/summarytable','bin/summarytable_ap',],
    url='https://www.github.com/dalekreitler-bnl/summarytable',
    license='LICENSE.txt',
    description='Gathering MX processing summaries',
    long_description=open('README.md').read(),
    install_requires=[
        "xmltodict",
        "python>=3.8",
    ],
)
