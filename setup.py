# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    author="Reece Hart <reecehart@gmail.com>",
    description="ensures that the `reece` package is available only as a namespace package",
    name="reece",
    packages=find_packages(),
    url="https://github.com/reece/reece-namespace-declaration",
    version='0.0.0',
    zip_safe=True,
)
