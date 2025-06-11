from setuptools import setup, find_packages

setup(
    name='autostack',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'rich',
        'Jinja2',
    ],
    entry_points={
        'console_scripts': [
            'autostack = autostack.main:cli',
        ],
    },
) 