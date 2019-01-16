# from distutils.core import setup
from setuptools import find_packages, setup

setup(
    name='controlM-rest',
    version='0.1.5',
    packages=find_packages(),
    long_description=open('README.txt').read(),
    keywords=['ControlM', 'REST-api'],
    python_requires='>=2.7',
    install_requires=['requests >= 2.8, < 3.0.0a0'],
    entry_points={
        'console_scripts': [
            'ctrlm = controlm_rest_api.ctrlM:main' 
        ]
    }
)