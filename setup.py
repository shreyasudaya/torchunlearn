from setuptools import find_packages, setup

setup(
    name='torchunlearn',
    packages=find_packages(include=['torchunlearn']),
    version='0.1.0',
    description='A library for Machine Unlearning in Pytorch',
    author='Shreyas Udaya',
    install_requires=['torch'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)