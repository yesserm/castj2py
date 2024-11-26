from setuptools import setup, find_packages

setup(
    name='cast_j2py',
    version='0.1.0',
    packages=find_packages(
        where='src',
        exclude=['tests']
    ),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter'
    ],
    entry_points={
        'console_scripts': [
            'cast_j2py=main:main'
        ]
    }
)
