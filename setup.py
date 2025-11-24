from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based Books Recommender System"
SRC_REPO = "books_recsys_end-to-end"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamalla/books_recsys_end-to-end",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.11",
    install_requires=LIST_OF_REQUIREMENTS
)