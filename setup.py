

from setuptools import setup, find_packages


with open('READme.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


AUTHOR_NAME = 'AUGUSTIN'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

# streamlit is a open source framework of python which converts the python scripts to attractive web apps



setup(
    name = SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='augustin7766@gmail.com',
    description='A small example package for movies recommendation',
    long_description=long_description
)