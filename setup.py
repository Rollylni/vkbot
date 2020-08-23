#!/usr/bin/env python

"""Library for creating VK Bots"""
from setuptools import setup
############
import vkbot

description = open("README.rst").read()

setup(
    name="vkbot",
    author=vkbot.__author__,
    version=vkbot.__version__,
    license=vkbot.__license__,
    packages=["vkbot"],
    keywords="vkbot",
    description=__doc__,
    author_email="dimadersekt@gmail.com",
    url="https://github.com/Rollylni/vkbot",
    long_description=description,
    install_requires=["vk_api"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Natural Language :: Russian'
    ]
)