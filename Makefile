
init:
	./init.sh

freeze:
	pip freeze -l > requirements.txt

test:
	pytest

lint:
	pylint src

pylintrc:
	pylint --generate-rcfile > .pylintrc
