.PHONY: clean test build
VENV_DIR=venv

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@echo 'Removing pyc files'

build:
	@echo "Building project"
	@echo "Checking for previous virtual environment"
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "Deleting previous virtual environment"; \
		rm -rf $(VENV_DIR); \
	fi;
	@echo "Creating new virtual environment"
	@virtualenv $(VENV_DIR);
	@echo "Installing requirements"
	@source $(VENV_DIR)/bin/activate; \
	pip install -r requirements.txt; \
	deactivate;
	@echo "Finished building project"

test:
	@echo 'Running tests'
	@echo 'Activating virtualenv'
	@source $(VENV_DIR)/bin/activate; \
	python run_test.py
	@echo 'Test finished , please check log for more information'
