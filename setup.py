#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import pip
from setuptools import setup, find_packages


    # pip >=20
try:
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


with open('README.md') as f:
    readme = f.read()

# Handle requirements
requires = parse_requirements("requirements/install.txt", session=PipSession())
install_requires = [str(ir.requirement) for ir in requires]

requires = parse_requirements("requirements/tests.txt", session=PipSession())
tests_require = [str(ir.requirement) for ir in requires]

# Convert markdown to rst
try:
    from pypandoc import convert
    long_description = convert("README.md", "rst")
except:
    long_description = ""

version = ''
with open('rest_framework_gis_distance/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

setup(
    name="djangorestframework-gis-distance",
    version=version,
    description=(""),
    long_description=long_description,
    author="Fröjd",
    author_email="martin@marteinn.se",
    url="https://github.com/Frojd/restframework-gis-distance",
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    license="MIT",
    zip_safe=False,
    classifiers=(
        "Development Status :: 4 - Beta",
        'Environment :: Web Environment',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        "Programming Language :: Python :: 2.7",
        'Framework :: Django',
        'Topic :: Utilities',
    ),
)
