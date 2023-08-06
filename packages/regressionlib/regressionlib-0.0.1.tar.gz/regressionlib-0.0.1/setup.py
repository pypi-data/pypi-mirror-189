import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="regressionlib",
    version="0.0.1",
    author="Valery Drozd",
    author_email="drozdllera@gmail.com",
    description="Regression library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ValeryDrozd/regressionlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)