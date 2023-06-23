import os
from typing import List

import setuptools


def _parse_requirements(path: str) -> List[str]:
    """Returns content of given requirements file."""
    with open(os.path.join(path)) as f:
        return [
            line.rstrip() for line in f if not (line.isspace() or line.startswith("#"))
        ]


setuptools.setup(
    name="languadetectio",
    version="0.1.0",
    author="Aymen Krifa",
    author_email="aymenkrifa@gmail.com",
    description="Fast and Accurate Language Detection for Textual Data. Identify the language of text with precision using state-of-the-art techniques. Powered by FastText and FastAPI.",
    url="https://github.com/aymenkrifa/LinguaDetectio",
    long_description=open("README.md").read(),
    keywords="fastext language_detection fastapi python",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=_parse_requirements("requirements.txt"),
    package_data={"jumanji": ["py.typed"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
