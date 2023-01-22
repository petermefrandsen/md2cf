from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="md2cf",
    version="1.5.1",
    packages=["md2cf"],
    url="https://github.com/iamjackg/md2cf",
    license="MIT",
    author="Jack Gaino",
    author_email="md2cf@jackgaino.com",
    description="Convert Markdown documents to Confluence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="markdown confluence",
    install_requires=[
        "rich-argparse==1.0.0",
        "rich==13.0.1",
        "mistune==0.8.4",
        "chardet==5.1.0",
        "tortilla==0.5.0",
        "PyYAML==6.0",
        "gitignore_parser==0.0.8",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["md2cf=md2cf.__main__:main"]},
)
