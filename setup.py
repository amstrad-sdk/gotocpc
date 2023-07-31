from setuptools import setup, find_packages
from gotocpc import __version__ as version

VERSION = version
DESCRIPTION = 'Software Developer Kit for programming in Basic for Amstrad CPC'

setup(
    name='gotocpc',
    version=VERSION,
    author="Destroyer",
    author_email="<destroyer.dcf@gmail.com>",
    description=DESCRIPTION,
    license="GPL",
    packages=find_packages(),
    package_data={
        'bin': [
            'bin/linux/iDSK',
            'bin/linux/martine'],
# include gotocpc/bin/darwin/iDSK
# include gotocpc/bin/darwin/martine
# include gotocpc/bin/win/iDSK.exe
# include gotocpc/bin/win/martine.exe
# include gotocpc/bin/win/cyggcc_s-1.dll
# include gotocpc/bin/win/cygwin1.dll
        'includes': ['includes/*'],
        'templates': ['templates/*']
    },
    install_requires=[
        'click',
        'configparser',
        'rich',
        'PyYAML',
        'jinja2'
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
            'gotocpc=gotocpc.__main__:main',
            'go2cpc=gotocpc.__main__:main'
        ]
    }
)