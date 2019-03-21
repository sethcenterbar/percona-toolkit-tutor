from setuptools import setup, find_packages

setup(
    name='ptt',
    version='0.1',
    py_modules=['ptt'],
    install_requires=[
        'Click',
        'colorama',
        'PyYAML'
    ],
    entry_points='''
        [console_scripts]
        ptt=ptt:cli
    ''',
)
