from setuptools import setup

setup(
    name='golem',
    version='0.1.0',
    py_modules=['golem'],
    install_requires=[
        'Click',
    ],
    entry_points='''
    [console_scripts]
    golem=golem:cli
    ''',
)
