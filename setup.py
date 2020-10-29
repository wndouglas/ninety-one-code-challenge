from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="num_conv",
    version="0.0.1",
    description="num_conv is a package for converting lines of text containing digits into word-based numbers.",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/wndouglas/ninety-one-code-challenge",
    author="Will Douglas",
    author_email="wndouglas@hotmail.co.uk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8'
)
