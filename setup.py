import os
import re
from setuptools import find_packages, setup


PKG = "map_ops"
VERSIONFILE = os.path.join(PKG, "_version.py")
AUTHOR = "Kyle Emrick"
GITID = "kremrik"


def get_version() -> str:
    verstr = "unknown"

    try:
        verstrline = open(VERSIONFILE, "rt").read()
    except EnvironmentError:
        pass  # no file
    else:
        VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
        mo = re.search(VSRE, verstrline, re.M)
        if mo:
            verstr = mo.group(1)
        else:
            raise RuntimeError("Error loading version")
    
    return verstr


setup(
    name=PKG,
    version=get_version(),
    author=AUTHOR,
    url="https://github.com/{}/{}".format(GITID, PKG),
    description="A simple, but high-powered, module for operating on dictionaries and mapping types",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("docs")),
    include_package_data=True,
)
