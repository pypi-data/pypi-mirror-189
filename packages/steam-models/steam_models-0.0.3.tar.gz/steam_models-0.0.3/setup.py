from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='steam_models',
    version="0.0.3",
    author="STEAM Team",
    author_email="steam-team@cern.ch",
    description="Source code for APIs for STEAM tools.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://gitlab.cern.ch/steam/steam_models",
    keywords={'STEAM', 'simulation', 'modeling', 'CERN'},
    install_requires=["numpy"],
    extras_require={"dev": ["pandas", "matplotlib",],},
    python_requires='>=3.8',
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8"],

)
