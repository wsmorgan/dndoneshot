#!/usr/bin/env python
try:
    from setuptools import setup
    args = {}
except ImportError:
    from distutils.core import setup
    print("""\
*** WARNING: setuptools is not found.  Using distutils...
""")

from setuptools import setup
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from os import path
setup(name='dndoneshot',
      version='0.0.1',
      description='Code to help write DnD One Shots.',
      long_description= "" if not path.isfile("README.md") else read_md('README.md'),
      author='Wiley S Morgan',
      author_email='wiley.s.morgan@gmail.com',
      url='https://github.com/wsmorgan/dndoneshot',
      setup_requires=['pytest-runner',],
      tests_require=['pytest',],
      install_requires=[
      ],
      packages=['dndoneshot'],
      scripts=[''],
      package_data={'dndoneshot': []},
      include_package_data=True,
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Natural Language :: English',
          'Operating System :: MacOS',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7',
      ],
     )
