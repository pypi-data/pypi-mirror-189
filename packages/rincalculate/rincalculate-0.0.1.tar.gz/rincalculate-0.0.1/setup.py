from setuptools import setup
import setuptools

with open("README.md","r")as fh:
    long_description = fh.read()

setup(  
    name = 'rincalculate',
    version = '0.0.1',
    author = 'Rinchen',
    author_email ='rinchen1234@example.com',
    description = 'A small calculate package',
    long_description=long_description,
    long_description_content_type = "text/markdown",
    # url = https://github.com/pypa/sampleproject
    packages=setuptools.find_packages(),
    keywords=["calculate","cal"],
    classifiers =[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires ='>=3.6',

    py_modules=['rincalcu'],
    package_dir={'':'src'},
    install_requires= 'python-math',
    
)            