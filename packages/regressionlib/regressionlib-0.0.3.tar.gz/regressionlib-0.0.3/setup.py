import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name="regressionlib",
    version="0.0.3",
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
    install_requires=REQUIREMENTS
)