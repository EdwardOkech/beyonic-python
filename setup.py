import os
import sys
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

VERSION = "0.1.3a1"

setup(
    name="beyonic",
    version=VERSION,
    description="The official Python client for the Beyonic.com API",
    author="Beyonic",
    author_email="info@beyonic.com",
    long_description=long_description,
    packages=["beyonic", "beyonic.apis"],
    install_requires=["requests"],
    license="MIT",
    keywords=["api", "mobile payments", "mobile money", "beyonic", "mpesa"],
    url="http://beyonic.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
