from setuptools import setup, find_packages

setup(
    name="barte-python-sdk",
    version="0.1.0",
    description="Python SDK for integration with Barte API",
    author="Thiago Avelino",
    author_email="thiago.avelino@buser.com.br",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "dacite>=1.8.0",
        "python-dateutil>=2.8.0"
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
) 