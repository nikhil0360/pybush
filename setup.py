from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pybush',
    version = '1.1.0',
    py_modules = ['pybush'],
    author = 'nikhil agarwal',
    url='https://github.com/nikhil0360',
    author_email = 'nikhil.agarwal@iiitb.org',
    description='python implementation of avl,bbst,bst and more',
    install_requires=['binarytree'],
    download_url = 'https://github.com/nikhil0360/pybush/archive/v1.1.0.tar.gz',
    long_description=readme(),
    long_description_content_type="text/markdown"
)

