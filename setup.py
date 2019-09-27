from os.path import dirname, join
from pkg_resources import parse_version
from setuptools import setup, find_packages, __version__ as setuptools_version

extras_require = {}

setup(
    name='testproj',
    version=1.0,
    url='https://scrapy.org',
    description='test project for test',
    author='solinari',
    maintainer='No one',
    maintainer_email='No one',
    license='None',
    packages=find_packages(exclude=('test', 'Log', 'mlrun')),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'numpy',
        'pandas',
        'torch>=1.0',
    ],
    extras_require=extras_require,
)