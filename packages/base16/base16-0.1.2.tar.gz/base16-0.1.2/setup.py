'''
Setup script for the package.
'''

from setuptools import setup, find_packages

setup(
    name='base16',
    author='Philip Orange',
    email='pypi@philiporange.com',
    url='https://www.github.com/philiporange/base16',
    version='0.1.2',
    description='''
base16 is like hexadecimal, but with an alphabet chosen to minimise human transcription errors.
''',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=['base16'],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'base16 = base16.__main__:main',
        ],
    },
    classifiers=[
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
)
