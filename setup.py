from setuptools import setup

setup(
    name='nmctl',
    version='0.1',
    py_modules=['nm'],
    install_requires=[
        'click==7.1',
        'pandas==0.24.2',
    ],
    entry_points={'console_scripts': [
        'nmctl=nm.nmctl:cli'
    ]}
)