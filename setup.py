#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="litex_on_profpga_systems",
    description="Infrastructure to create SoCs based on proFPGA systems and LiteX",
    author="LiteX on proFPGA Systems Developers",
    url="https://github.com/litex-hub",
    download_url="https://github.com/litex-hub/litex-on-profpga-systems",
    test_suite="test",
    license="BSD",
    python_requires="~=3.6",
    packages=find_packages(exclude=("test*", "sim*", "doc*", "examples*")),
    include_package_data=True,
)
