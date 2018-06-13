from setuptools import setup, find_packages

setup(
    name='fasth',
    version='0.1',
    packages=find_packages(),
    scripts=['fasth.py'],

    install_requires=[],

    author='Jordan Gumm',
    author_email='jordan@variantanalytics.com',
    description='A tool for quick fasta/fastq calculations'
)
