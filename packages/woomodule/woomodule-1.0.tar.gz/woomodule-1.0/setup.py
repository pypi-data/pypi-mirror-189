from setuptools import setup, find_packages
from os.path import join, dirname


with open("requirements.txt") as dependency:
    requirements = dependency.read()


setup(
    name='woomodule',
    version="1.0",
    author="Dihtiar Vadym",
    description="Package for practice",
    test_suite='tests',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    entry_points={'console_scripts': ['get_str = src.woomodule.app.app:get_str']},
)