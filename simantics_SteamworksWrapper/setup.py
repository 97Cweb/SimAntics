from setuptools import setup, find_packages

setup(
    name="simantics_SteamworksWrapper",
    version="0.1.0",
    description="Steam API wrapper for SimAntics",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),  # Automatically find and include the 'steam_wrapper' package
    include_package_data=True,
    package_data={
        "steamworks_wrapper": [
            "steamworks_sdk_161/sdk/redistributable_bin/*",  # Include all files in the redistributable_bin folder
        ],
    },
    python_requires=">=3.6",
)
