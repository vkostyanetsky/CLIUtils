#!/usr/bin/env python3

from setuptools import setup
from fastimer.version import __version__


setup(
    name="cliutils",
    version=__version__,
    description="A simple library of functions intended to make console applications development a bit faster.",
    long_description=open("README.md", encoding="utf-8-sig").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vkostyanetsky/CliUtils",
    license="MIT",
    python_requires=">=3.7",
    packages=["cliutils"],
    install_requires=[],
    entry_points={"console_scripts": ["fastimer=fastimer.fastimer:main"]},
    author="Vlad Kostyanetsky",
    author_email="vlad@kostyanetsky.me",
    # https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
    keywords="cli console menu progressbar",
)
