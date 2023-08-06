from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'arman_k'
LONG_DESCRIPTION = """This package made by Arman Kumar 
This package helps you to perform great operations
1. It helps you to convert Binary to decimal
2. It helps you to make fibonacci series """

# Setting up
setup(
    name="arman_k",
    version=VERSION,
    author="Arman",
    author_email="armank3001@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['binary', 'math', 'mathematics', 'k.v.ofdumdum', 'arman kumar'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)