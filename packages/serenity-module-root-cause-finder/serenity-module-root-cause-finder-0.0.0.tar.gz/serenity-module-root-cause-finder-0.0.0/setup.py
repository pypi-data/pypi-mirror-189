import os
from setuptools import setup

version = "0.0.0"

setup(
    name=os.environ.get('PACKAGE_NAME', ''),
    version=version,
)
