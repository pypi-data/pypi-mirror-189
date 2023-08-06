from setuptools import setup 
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name="Grayscale Converter",version="0.5",
description="This is a grayscale converter package with custom extension version 0.5",
long_description=long_description,
    long_description_content_type="text/markdown",
author=["Pranav Singh","Aashutosh Dubey","Aditya Singh Rathore"],
author_email="psingh2_be20@thapar.edu",
packages=['greyscale_pack'],
install_requires=['PILLOW'],
include_package_data=True,
    entry_points={
        "console_scripts": [
            "greyScale=greyscale_pack.greyscale:main",
        ]
    }
)