#!/usr/bin/env python
import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
        name='qubolite',
        packages=['qubolite'],
        version='0.6.10',
        description='Toolbox for quadratic binary optimization',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Sascha Muecke',
        author_email='sascha.muecke@tu-dortmund.de',
        url='https://github.com/smuecke/qubolite',
        install_requires=['numba>=0.55.2','numpy>=1.23.5'],
        python_requires='>=3.8'
)
