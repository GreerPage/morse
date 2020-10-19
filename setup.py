
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="morse",
    version="0.1.1",
    author="Greer Page",
    author_email="greerishere@gmail.com",
    description="morse code for raspberry pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GreerPage/morse",
    packages=setuptools.find_packages(),
    install_requires=["raspi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    entry_points={
        "console_scripts": [
            'morse = morse:main',
        ],
    },
)