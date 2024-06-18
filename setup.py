from setuptools import setup, find_packages

setup(
    name='cli_tool',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        cli_tool=cli_tool:cli
    ''',
)
