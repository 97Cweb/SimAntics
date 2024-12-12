from setuptools import setup, find_packages
import os

# Define paths to include in package data
def find_package_data(package, root_dirs):
    """Recursively include all files in the specified directories."""
    data_files = []
    for root_dir in root_dirs:
        for dirpath, _, filenames in os.walk(os.path.join(package, root_dir)):
            for filename in filenames:
                full_path = os.path.relpath(os.path.join(dirpath, filename), package)
                data_files.append(full_path)
    return data_files


setup(
    name="steamworks_wrapper",
    version="0.1.0",
    description="Steamworks integration for Simantics",
    author="Your Name",
    author_email="your.email@example.com",
    packages=["steamworks_wrapper"],  # Explicitly include only this module
    package_dir={"steamworks_wrapper": "src/steamworks_wrapper"},  # Map the package directory
    include_package_data=True,
    package_data={
        "steamworks_wrapper": find_package_data("src/steamworks_wrapper", ["steamworks_sdk_161"]),
    },
    python_requires=">=3.6",
)
