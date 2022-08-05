from setuptools import setup

from utils import version


# Read description
with open("README.md", "r") as readme:
    README_TEXT = readme.read()

# main setup configuration class
setup(
    name="marketplace_user_docs",
    version=version,
    author="The MarketPlace Consortium",
    description="MarketPlace user docs",
    keywords="MarketPlace, documentation, sphinx",
    long_description=README_TEXT,
)
