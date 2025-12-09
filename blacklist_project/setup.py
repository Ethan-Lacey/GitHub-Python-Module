from setuptools import setup, find_packages

setup(
    name="blacklist",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        #no external dependencies needed for this script
    ],
    entry_points={
        "console_scripts": [
            "blacklist = blacklist.cli:commandLine",
        ],
    },
)