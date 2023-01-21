PYTHON = python3

.PHONY = help setup

.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "------------------------------------"

setup:
	@echo "Setting up the project"
	@pip install -e .
	@echo "Installing requirements"
	@pip install -r requirements.txt
	@echo "Successfully installed requirements"
