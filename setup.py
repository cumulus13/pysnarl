#!/usr/bin/env python

from distutils.core import setup
import PySnarl

setup(
    name            = 'PySnarl',
    version         = PySnarl.__version__,
    description     = 'A Snarl binding for Python',
    download_url    = 'http://code.google.com/p/pysnarl/downloads/list',
    author          = 'Sam Listopad II',
    author_email    = 'samlii@users.sourceforge.net',
    url             = 'http://code.google.com/p/pysnarl/',
    packages        = ['PySnarl'],
    license         = 'Apache License, Version 2.0',
    long_description = """
A Python extension exposing the main functions of the Snarl API.

Usage

This module can be used in two ways. One is the normal way the other interfaces work. This means you can call snShowMessage and get an ID back for manipulations.

The other way is there is a class this module exposes called SnarlMessage. This allows you to keep track of the message as a python object. If you use the send without specifying False as the argument it will set the ID to what the return of the last SendMessage was. This is of course only useful for the SHOW message.

Requirements

    * pywin32 extensions from PyWin32
    * ctypes from ctypes (Also included in Python 2.5 and up)
""",
    platforms = 'MS Windows',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Plugins',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Networking :: Monitoring :: Hardware Watchdog',
        'Topic :: Utilities',
    ],
)
