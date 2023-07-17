"""A setuptools based setup module."""

from setuptools import setup, find_packages

setup(
    name="tessiepy",
    version="0.0.4",
    description="A Python API for Tessie",
    url="https://github.com/cbzink/tessiepy",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="Tessie",
    install_requires=["aiohttp"],
    author="Charles Zink",
    author_email="charleszink@gmail.com",
    packages=find_packages(include=["tessiepy"]),
    py_modules=["tessiepy"],
)
