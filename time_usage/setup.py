import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="time_usage-pkg-Yannis", # Replace with your own username
    version="0.0.1",
    author="Yannis",
    author_email="nikoloudakis@pasiphae.eu",
    description="It measures the time it takes to complete a code-block",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)