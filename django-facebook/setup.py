from setuptools import setup, find_packages

setup(
    name = "django-facebook",
    version = "1.0",
    url = 'http://github.com/shantanaBernados/django-facebook',
    license = 'BSD',
    description = "A short URL handler for Django apps.",
    author = 'Shantana Bernados',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)