from setuptools import setup, find_packages

setup(
    name="mindflow",
    version="0.2.5",
    py_modules=["mindflow"],
    entry_points={"console_scripts": ["mf = mindflow.main:main"]},
    packages=find_packages(),
)
