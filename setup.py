from setuptools import setup

setup(
    name='rankm',
    version='0.1',
    py_modules=['rankm'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        rankm=rankm:cli
    ''',
)
