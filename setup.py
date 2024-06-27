from setuptools import setup, find_packages

setup(
    name='MyProject',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    entry_points={
        'console_scripts': []
    },
)