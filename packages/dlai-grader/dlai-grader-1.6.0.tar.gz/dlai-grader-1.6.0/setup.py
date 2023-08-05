from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="dlai-grader",
    version="1.6.0",
    description="Grading utilities for DLAI courses",
    url="https://github.com/https-deeplearning-ai/grader",
    author="Andres Zarta",
    author_email="andrezb5@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT License",
    packages=find_packages(),
    entry_points={
        "console_scripts": ["dlai_grader = dlai_grader.cli:parse_dlai_grader_args"]
    },
    install_requires=[
        "nbformat>=5.1.3",
        "jupytext>=1.13.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
