from setuptools import setup, find_packages

setup(
    name='golem',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'SQLAlchemy',
    ],
    entry_points='''
    [console_scripts]
    golem=scripts.run:cli
    ''',
)
