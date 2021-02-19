# -*- coding: utf-8 -*-
import io

from setuptools import find_packages, setup
from Semi_ATE.TnD import __version__

# =============================================================================
# Use README.md for long description
# =============================================================================
with io.open("README.md", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="Semi-ATE-TnD",
    version=__version__,
    description="Convenient Date and Time library for python",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Tom Hören",
    maintainer="Semi-ATE",
    maintainer_email="info@Semi-ATE.com",
    url="https://github.com/Semi-ATE/DT",
    license="MIT",
    keywords="Semiconductor ATE Automatic Test Equipment Date Time",
    platforms=["Windows", "Linux", "Mac OS-X"],
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
    ],
)
