from setuptools import setup, find_packages

setup(
    name="bright_spark_cli_tool",
    version="1.0",
    packages=find_packages(),
    py_modules=["cli_tool"],
    install_requires=[
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "cli_tool=cli_tool:main",
        ],
    },
    author="Ceri Nguyen",
    author_email="sn10101994@gmail.com",
    description="A CLI tool for processing CSV records and outputting top records in YAML or JSON format",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
