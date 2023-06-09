VENV_DIR := .venv
PYTHON := ${VENV_DIR}/bin/python

clean:
	rm -rf $(VENV_DIR)

venv: $(PYTHON)
$(PYTHON): setup.py
	test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .