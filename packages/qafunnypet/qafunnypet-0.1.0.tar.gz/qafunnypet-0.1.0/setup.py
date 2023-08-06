import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="qafunnypet",
    version="0.1.0",
    author="Daniel Mendez",
    author_email="pablomen1131@gmail.com",
    description="Testing a package that can be inherit to classes that use it",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/danielmen-mx/qafunnypet",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=setuptools.find_packages()
)
