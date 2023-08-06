# Change the content according to your package.
import setuptools
import re
import os

# Extract the version from the init file.
VERSIONFILE = "twinpackage/__init__.py"
getversion = re.search(
    r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSIONFILE, "rt").read(), re.M)
if getversion:
    new_version = getversion.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

# Configurations
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
        'wfdanielpackagetest'
    ],
    python_requires='>=3',
    name='twinpackagedani',
    version=new_version,
    author="D.Mendez",
    author_email="pablomen1131@gmail.com",
    description="Python package for my twinpackagedani.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/danielmen-mx/twinpackagedani",
    download_url='https://github.com/danielmen-mx/twinpackagedani/archive/'+new_version+'.tar.gz',
    packages=setuptools.find_packages(),
    include_package_data=True,
    license_files=["LICENSE"],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
