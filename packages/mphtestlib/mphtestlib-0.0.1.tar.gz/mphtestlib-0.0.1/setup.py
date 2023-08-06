import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mphtestlib",
    version="0.0.1",
    author="Michael Medvediev",
    author_email="misha.medvediev2001@gmail.com",
    description="MPH Test Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MedvedMichael/mph_test_lib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
