from setuptools import setup, find_packages

setup(
    py_modules = ['generator'],
    
    install_requires = [],
    packages = find_packages(include=["datapack_generator", "datapack_generator.*"])
)