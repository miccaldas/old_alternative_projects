from setuptools import setup

setup(
    name="books",
    version=2.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="CRUD scripts for book management.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/python_project_mclds",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["books"],
    install_requires=[
        "urwid",
    ],
    include_package_data=True,
)
