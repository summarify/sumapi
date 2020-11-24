import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sumapi",
    version="0.0.2",
    author="Summarify",
    author_email="info@summarify.io",
    description="API Library for SumAPI with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/summarify/sumapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5.5',
    install_requires=["requests==2.21.0"])
