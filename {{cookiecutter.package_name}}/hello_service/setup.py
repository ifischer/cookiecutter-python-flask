from setuptools import setup, find_packages

setup(
    name='hello_service',
    description='hello_service',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'Flask',
    ],
    python_requires='>=3.7'
)
