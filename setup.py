"""
Setup script for Research Paper Figure Generator
===============================================

A Python toolkit for creating publication-ready figures for research papers.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="research-figure-generator",
    version="1.0.0",
    author="Research Team",
    author_email="research@example.com",
    description="A Python toolkit for creating publication-ready figures for research papers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oninoor2000/figures",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "generate-clinic-figures=clinic_distribution:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 