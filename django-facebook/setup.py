from setuptools import setup, find_packages

setup(
    name="django-facebook",
    version="1.0",
    url='https://github.com/shantanaBernados/facebook_wall',
    license='BSD',
    description="A mini project for training.",
    author='Shantana Bernados',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
)
