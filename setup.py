#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name="oaic-samplexapp-test1",
    version="0.0.1",
    packages=find_packages(exclude=["tests.*", "tests"]),
    description="oaic xApp for test",
    url="https://github.com/mrkouchaki/oaic-samplexapp-test1",
    install_requires=["ricxappframe>=1.1.1,<3.0.0", "ricsdl==3.1.1", "pandas>=1.1.3", "joblib>=0.3.2", "Scikit-learn>=0.21", "schedule>=0.0.0", "influxdb", "p5py", "PEP517", "Cython", "numpy >= 1.16.2", "ipython", "tensorflow", "redis", "statistics", "matplotlib", "gym", "pygame", "typing", "shapely", "svgpath2mpl", "abcplus"],
    entry_points={"console_scripts": ["run-mr.py=mr.main:start"]},  # adds a magical entrypoint for Docker
    license="Apache 2.0",
    data_files=[("", ["LICENSE.txt"])],
)

