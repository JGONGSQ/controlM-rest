from distutils import setup

setup(
    name='controlM-rest',
    version='0.1',
    packages=['controlm-rest-api',],
    author='James Gong',
    long_description=open('README.md').read(),
    keywords=['ControlM', 'REST-api'],
    python_requires='>=2.7',
    install_requires=['requests >= 2.8, < 3.0.0a0'],
)