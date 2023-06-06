from setuptools import setup, find_packages
from pc2cpc import __version__ as version

VERSION = version
DESCRIPTION = 'Software Developer Kit for programming in Basic for Amstrad CPC'

setup(
    name='pc2cpc',
    version=VERSION,
    author="Destroyer",
    author_email="<destroyer.dcf@gmail.com>",
    description=DESCRIPTION,
    license="GPL",
    packages=find_packages(),
    install_requires=[
        'click',
        'configparser',
        'rich'
    ],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',   
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'pc2cpc= pc2cpc.__main__:main',
        ]
    }
)