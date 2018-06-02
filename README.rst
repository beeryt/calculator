Material Calculator
==========

A basic materials calculator supporting various units.

Install
-------

	python3 -m venv venv
	. venv/bin/activate
	pip install -e .

Run
---

::

	Calculator

Test
----

::

	pip install '.[test]'
	pytest

	coverage run -m pytest
	coverage report
	coverage html