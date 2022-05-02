from setuptools import setup

setup(
    name="tree",
    version=4.0,
    author="mclds",
    author_email="mclds@protonmail.com",
    description="Tree file visualiser. Taken from the Rich documentation",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://codeberg.org/micaldas/tree",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["tree"],
    install_requires=[
        "rich",
        "snoop",
        "click",
    ],
    include_package_data=True,
    entry_points={
        "console_scripts": ["ntree = tree.ntree:walk_directory"],
    },
)
