from setuptools import setup

version = '0.0.1'

setup(
    name='cortex',
    version=version,
    author='Worldbrain contributors',
    author_email='dev@worldbrain.io',
    description='back-end for webmarks',
    url='https://github.com/WorldBrain/cortex',
    packages=('worldbrain',),
    include_package_data=True,
)
