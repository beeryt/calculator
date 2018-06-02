import io

from setuptools import find_packages, setup

with io.open("README.rst", "rt", encoding="utf8") as f:
	readme = f.read()


setup(
	name="calculator",
	version="0.2dev",
	author="T. Carl Beery",
	author_email="beeryt@oregonstate.edu",
	description="A materials calculator.",
	long_description=readme,
	packages=[
		"src/calculator",

	],
	extras_require={
		'test': [
			'pytest',
			'coverage',
		],
	},
)