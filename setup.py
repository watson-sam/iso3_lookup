#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name="iso3_lookup",
    version="0.1.0",  # Defined in version.txt
    packages=find_packages(),
    entry_points={
        "console_scripts": ["NA"]
    },
    install_requires=[],
    # metadata for upload to PyPI
    author="Sam Watson",
    author_email="Please ask.",
    description="Go from iso3 -> country name and visa versa",
    url="https://github.com/watson-sam/iso3_lookup",
)
