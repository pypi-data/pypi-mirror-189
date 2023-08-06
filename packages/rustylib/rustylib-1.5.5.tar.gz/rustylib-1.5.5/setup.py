from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["requests==2.27.1"]


setup(
    name="rustylib",
    version="1.5.5",
    author="ZeyaTsu",
    description="A comprehensive utility library for Python, featuring modules for color manipulation, mathematical operations, random number generation, HTTP requests, mathematics, and a versatile utility module. Streamline your workflow with this all-in-one toolbox.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeyaTsu/rusty",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
