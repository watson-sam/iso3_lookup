#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name="iso3_lookup",
    version="0.3.0",  # Defined in version.txt
    packages=find_packages(),
    # metadata for upload to PyPI
    author="Sam Watson",
    author_email="quadquants@gmail.com",
    description="Go from iso3 -> country name and visa versa",
    url="https://github.com/watson-sam/iso3_lookup",
)
