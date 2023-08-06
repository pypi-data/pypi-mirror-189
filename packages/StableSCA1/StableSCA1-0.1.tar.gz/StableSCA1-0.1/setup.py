from setuptools import setup, find_packages

setup(
    name='StableSCA1',
    version='0.1',
    author='Stabel',
    author_email='support@stabel.tech',
    description='An in-line smart contract audit tool',
    packages=find_packages(),
    install_requires=[
        'requests',
        'web3'
    ],
)
 
