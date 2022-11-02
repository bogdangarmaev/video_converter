#!/usr/bin/env python

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import distutils
import subprocess
from os.path import dirname, join

from setuptools import find_packages, setup


def read(*args):
    return open(join(dirname(__file__), *args)).read()


class ToxTestCommand(distutils.cmd.Command):
    """Distutils command to run tests via tox with 'python setup.py test'.

    Please note that in our standard configuration tox uses the dependencies in
    `requirements/dev.txt`, the list of dependencies in `tests_require` in
    `setup.py` is ignored!

    See https://docs.python.org/3/distutils/apiref.html#creating-a-new-distutils-command
    for more documentation on custom distutils commands.
    """

    description = "Run tests via 'tox'."
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.announce("Running tests with 'tox'...", level=distutils.log.INFO)
        return subprocess.call(["tox"])


exec(open("video_converter/version.py").read())

install_requires = []

tests_require = [
    "coverage",
    "flake8",
    "pydocstyle",
    "pylint",
    "pytest-pep8",
    "pytest-cov",
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    "pytest",
]

exec(read("video_converter", "version.py"))


setup(
    name="video_converter",
    version=__version__,  # noqa
    description="Video converter",
    long_description=read("README.md"),
    author="bogdan",
    author_email="bogdangarmaev@gmail.com",
    url="https://github.com/yourname/video_converter",
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
    ],
    include_package_data=True,
    install_requires=install_requires,
    packages=find_packages(include=["video_converter*"]),
    test_suite="tests",
    setup_requires=["pytest-runner"],
    tests_require=tests_require,
    cmdclass={
        "test": ToxTestCommand,
    },
)
