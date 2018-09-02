from setuptools import setup, find_packages

setup(
    name="orlocal",
    version="0.0.2",
    summary='InfoSystem Seed',
    description="InfoSystem Seed Flask REST service",
    packages=find_packages(exclude=["tests"])
)
