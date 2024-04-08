from setuptools import setup, find_packages

setup(
    name="poi_simulator",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    python_requires=">=3.8",
    author="Thomas Mueller",
    author_email="tommail5@t-online.de",
    description="A simple simulator for Poi",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    url="",  # Add your project's URL
    classifiers=[
        "Programming Language :: Python",
    ],
    entry_points={
        "gui_scripts": [
            "poi-simulator = poi_simulator.poi_simulator:main",
        ],        
    },
)