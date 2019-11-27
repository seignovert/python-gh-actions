"""Foo setup."""

from pathlib import Path

from setuptools import find_packages, setup


HERE = Path(__file__).parent
README = (HERE / 'README.md').read_text()
VERSION = (HERE / 'foo' / '__version__.py').read_text().split("'")[1]


setup(
    name='foo',
    version=VERSION,
    description='Foo test module',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/seignovert/foo',
    author='Benoit Seignovert',
    author_email='dev@seignovert.fr',
    license='MIT',
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    include_package_data=True,
    install_requires=[],
    packages=find_packages(exclude=['tests']),
)
