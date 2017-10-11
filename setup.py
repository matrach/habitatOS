import os
import sys
from setuptools import setup, find_packages
from os import path


assert sys.version_info >= (3, 6), "Python 3.6+ required."


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(path.join(BASE_DIR, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='HabitatOS',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.9.0',

    description='Analog space habitat operating system.',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/astromatt/HabitatOS',

    # Author details
    author='Matt Harasymczuk',
    author_email='HabitatOS@astrotech.io',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Operating System',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ],

    # What does your project relate to?
    keywords='space exploration analog analogue habitat operating system',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'contrib', 'tmp']),

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    package_data={
        # 'sample': ['__init__.py'],
    },

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pep8'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file.txt'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'habitatOS=HabitatOS:manage',
        ],
    },
)
