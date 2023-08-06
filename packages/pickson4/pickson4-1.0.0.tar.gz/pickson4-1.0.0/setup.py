from setuptools import setup

def readme():
    
    with open("README.md") as f:
        README = f.read()
        
    return README


setup(
    
    name = "pickson4",
    version="1.0.0",
    description = "A python package for saving and getting pickled and JSON data",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/MikeTeachesCode/pickson",
    author="Michael S. Russell",
    author_email="miketeachingcode@yahoo.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    
    packages = ["pickson4"],
    package_dir = {"pickson4": "pickson4"},
    include_package_data = False,
    install_requires=[]

)
    
    
   