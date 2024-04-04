ENV_DIR="venv"
PYTHON=python3.11

init:
	mkdir -p $(ENV_DIR)
	$(PYTHON) -m venv $(ENV_DIR)
	source $(ENV_DIR)/bin/activate ; pip install -r requirements.txt

clean:
	rm -rf $(ENV_DIR) 

freeze:
	pip freeze -l > requirements.txt

test:
	pytest

lint:
	pylint src

pylintrc:
	pylint --generate-rcfile > .pylintrc
