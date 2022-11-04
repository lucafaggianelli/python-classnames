#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

with open("CHANGELOG.md") as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    author="Luca Faggianelli",
    author_email="luca.faggianelli@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Utility to create CSS class strings from a multitude of values without poking around with string templates and lengthy logic.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="classnames",
    name="classnames",
    packages=find_packages(include=["classnames", "classnames.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/lucafaggianelli/python-classnames",
    version="0.1.0",
    zip_safe=False,
)
