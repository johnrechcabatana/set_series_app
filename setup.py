from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in set_series/__init__.py
from set_series import __version__ as version

setup(
	name='set_series',
	version=version,
	description='This app is useful for set setters',
	author='John Rech G. Cabatana',
	author_email='cabatana.johnrech.g@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
