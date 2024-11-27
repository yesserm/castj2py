from setuptools import setup, find_packages

setup(
    name='castj2py',
    version='0.1.0',
    author='Yesser Miranda',
    author_email='yesser.miranda0106@gmail.com',
    description='Convert JavaScript code to Python code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yesserm/castj2py',
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
            'castj2py=main:main'
        ]
    }
)
