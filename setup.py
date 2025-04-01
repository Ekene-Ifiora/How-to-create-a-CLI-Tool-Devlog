# setup.py

from setuptools import setup, find_packages

setup(
    name='devlog',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'pynvim'
    ],
    entry_points={
        'console_scripts': [
            'devlog=devlog.cli:cli',
        ],
    },
)
