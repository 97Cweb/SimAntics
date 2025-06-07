from setuptools import setup, find_packages

setup(
    name="simantics-common",
    version="0.1.0",
    description="Common utilities for SimAntics",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # Automatically find and include the 'common' package
    include_package_data=True,
    python_requires=">=3.6",
)
