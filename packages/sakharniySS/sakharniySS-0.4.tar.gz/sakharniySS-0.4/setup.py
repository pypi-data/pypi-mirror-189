from setuptools import setup, find_packages

setup(
    name='sakharniySS',
    version='0.4',
    author='Siarhei Sakharnyi',
    description='Combined package for feature extraction, hyperparameter tuning, and validation schema',
    packages=find_packages(),
    install_requires=['numpy', 'scikit-learn', 'hyperopt','pandas', 'fuzzywuzzy']
)
