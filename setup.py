from setuptools import setup, find_packages

from ru_rag import __version__


NAME = "ru-rag"
ROOT_PACKAGE = NAME.replace("-", "_")


setup(
    name=NAME,
    platforms="any",
    version=__version__,
    packages=find_packages(
        exclude=[f"{ROOT_PACKAGE}.tests", f"{ROOT_PACKAGE}.tests.*"]
    ),
    entry_points={
        "console_scripts": [
            f"populate_db = {ROOT_PACKAGE}.serve:populate_db",
            f"find_similar = {ROOT_PACKAGE}.serve:find_similar",
            f"answer = {ROOT_PACKAGE}.serve:answer",
        ],
    },
    install_requires=[
        # prod
        "chromadb==0.3.23",
        "huggingface-hub==0.14.1",
        "langchain==0.0.174",
        "llama-cpp-python==0.1.53",
        "sentence-transformers",

        # dev
        "autopep8",
        "black",
    ],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
)
