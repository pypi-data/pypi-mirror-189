import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="forced_url_modifier", # Replace with your own username
    version="0.0.7",
    author="dh kim",
    author_email="itschoolkdh@gmail.com",
    description="for URL forced FULL encoding & decoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/khgxsss/forced-url-modifier",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',

)