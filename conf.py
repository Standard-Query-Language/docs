import os
import sys

# conf.py for Read the Docs

sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Standard Query Language (SQLY)'
author = 'Antony Bailey'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

exclude_patterns = []

# Options for HTML output
html_theme = 'alabaster'
html_static_path = ['_static']
