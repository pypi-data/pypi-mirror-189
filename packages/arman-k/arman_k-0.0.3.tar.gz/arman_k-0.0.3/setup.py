from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'arman_k'

LONG_DESCRIPTION = """

# Performs Great Operations

This module is for creating great operations



## Author

- [@armank3001](https://www.github.com/armankumar2)



#
## Badges

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/armankumar2/module_creation/blob/main/LICENSE)

[![forthebadge made-with-python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

#
## Features

- It helps to perform fibonacci series
- It helps to convert binary into decimal

#
## Installation

Install arman-k with pip

```bash
  pip install arman-k
```

## Upgrade

Upgrade arman-k with pip

```bash
  pip install --upgrade arman-k
```
    
## Usage/Examples

```python
from arman_k import yo
yo.fibonacci(5)
yo.binary_to_decimal(1101)
```
#

## 📝 License
 This project is licensed under [MIT](https://github.com/armankumar2/module_creation/blob/main/LICENSE)
 license.

#
## Feedback  ✨

If you have any feedback, please reach out to us at armank3001@gmail.com

"""    

# Setting up
setup(
    name="arman_k",
    version=VERSION,
    author="Arman Kumar",
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