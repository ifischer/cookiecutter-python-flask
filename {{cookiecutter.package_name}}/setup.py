from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.package_name}}',
    description='{{cookiecutter.description}}',
    packages=find_packages(),
    version='0.0.1',
    install_requires=[
        'Flask',
    ],
    {%- if cookiecutter.python_version %}
    python_requires='>={{cookiecutter.python_version}}'
    {%- endif %}
)
