"""
    django-accountkit
    ~~~~~~~~~~~~~~~
"""
import re

from setuptools import setup

version = ''
with open('accountkit/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(), re.MULTILINE).group(1)

with open('README.md', 'r') as f:
    readme = f.read()
with open('HISTORY.rst', 'r') as f:
    history = f.read()

setup(
    name='django-accountkit',
    version=version,
    description='Allow easy integration with Facebook accountkit for Django projects',
    long_description=readme + '\n\n' + history,
    author='Pradip Caulagi',
    author_email='caulagi@gmail.com',
    url='http://github.com/toystori/django-accountkit/',
    packages=['accountkit'],
    package_data={'': ['LICENSE', 'HISTORY.rst']},
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
