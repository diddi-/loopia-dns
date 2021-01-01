import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LoopiaDNS",
    version="0.0.0",
    url="https://github.com/diddi-/python-loopiadns",
    author="Diddi Oskarsson",
    author_email="diddi@diddi.se",
    description="Library using the LoopiaDNS API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license="MIT",
    install_requires=[
        "click"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": ["loopia-dns=loopiadns.cli:main"]
    }
)
