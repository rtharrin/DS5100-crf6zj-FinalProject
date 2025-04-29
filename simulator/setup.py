from setuptools import setup, find_packages

setup(
    name='simulator',
    version='1.0.0',
    description='A Monte Carlo simulator package with Die, Game, and Analyzer classes',
    url='https://github.com/rtharrin/DS5100-crf6zj-FinalProject',
    author='Ryan Harrington',  
    license='MIT',
    packages=['simulator'],
    install_requires=[
        'numpy',
        'pandas'
    ]
)