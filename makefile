.PHONY: clean test build
VENV_DIR=venv
RED=`tput setaf 1`
GREEN=`tput setaf 2`
YELLOW=`tput setaf 3`
RESET=`tput sgr0`

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@echo 'Removing pyc files'

build:
	@echo "Building project"
	@echo "${YELLOW}Checking for previous virtual environment${RESET}"
	@if [ -d "$(VENV_DIR)" ]; then \
		echo "${RED}Deleting previous virtual environment${RESET}"; \
		rm -rf $(VENV_DIR); \
	fi;
	@echo "${GREEN}Creating new virtual environment${RESET}"
	@virtualenv $(VENV_DIR);
	@echo "${GREEN}Installing requirements${RESET}"
	@source $(VENV_DIR)/bin/activate; \
	pip install -r requirements.txt; \
	deactivate;
	@echo "Finished building project"

test:
	@echo 'Running tests'
	@echo 'Activating virtualenv'
	@source $(VENV_DIR)/bin/activate; \
	python run_test.py
	@echo "${GREEN}Test finished , please check log for more information${RESET}"
