#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='my_analysis_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',        # Add other dependencies as needed
        'numpy',
        'matplotlib',
    ],
    description='A Python package for data loading, cleaning, EDA, and visualizations',
    author='Your Name',
    author_email='your.email@example.com',
)

