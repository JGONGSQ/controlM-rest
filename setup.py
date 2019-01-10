from distutils.core import setup
from setuptools import find_packages

setup(
    name='controlM-rest',
    version='0.1.2',
    packages=find_packages(),
    long_description=open('README.txt').read(),
    keywords=['ControlM', 'REST-api'],
    # python_requires='>=2.7',
    install_requires=['requests >= 2.8, < 3.0.0a0'],
)