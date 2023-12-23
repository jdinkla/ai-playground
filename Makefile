
init:
	./init.sh

freeze:
	pip freeze -l > requirements.txt

lint:
	pylint src

pylintrc:
	pylint --generate-rcfile > .pylintrc
