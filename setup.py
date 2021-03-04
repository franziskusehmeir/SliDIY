from distutils.core import setup

from setuptools import find_packages

setup(
    name="slidiy",
    packages=find_packages(),
    version="0.0.1",
    description="An affordable slider system that can be controlled with a web app via a microcontroller. It can be easily reconstructed at home with the help of a manual.",
    author="Leon Tea & Franziskus Ehmeir",
    url="https://github.com/franziskusehmeir/SliDIY",
    keywords=["python", "stepper", "slider"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
    ],
)
