from pathlib import Path
from setuptools import setup

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='cryptogram',
    version='0.1',
    description='Solve Cryptograms',
    author='ASPdev',
    author_email='alexpdev@protonmail.com',
    license='GNU GPL3',
    packages=['cryptogram'],
    install_requires=[
        'PyQt6'
    ],
    zip_safe=False)
