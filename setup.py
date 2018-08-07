#!/usr/bin/env python3.5
from setuptools import setup

setup(name='remoteapp',
      version='0.1',
      description='Visualize sensor values from vibrabot data logging firmware',
      url='https://sourceforge.net/p/vibrabot/remoteapp/',
      author='Hochschule Karlsruhe',
      author_email='gnoc0001@hs-karlsruhe.de',
      packages=['remoteapp'],
      install_requires=['pyserial', 'matplotlib'],
      scripts=['bin/vibrabot-remoteapp.pyw', 'bin/legacy-remoteapp.py'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)