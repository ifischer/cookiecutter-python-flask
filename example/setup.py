from setuptools import setup, find_packages

setup(
    name='example',
    description='example',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'Flask',
    ],
    python_requires='>=3.7'
)
