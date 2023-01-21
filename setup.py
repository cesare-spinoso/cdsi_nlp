from distutils.core import setup

# README file contents
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cdsi_workshop_nlp',
    version='0.1dev',
    packages=['src',],
    license='MIT',
    description='CDSI Workshop on NLP ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=['Ines Arous', 'Cesare Spinoso-Di Piano'],
    author_email=['ines.arous@mila.quebec', 'cesare.spinoso-dipiano@mail.mcgill.ca'],
)