.PHONY: start
start:
	@echo "Starting the application..."
	pipenv run python src/manage.py runserver

.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit hooks..."
	pipenv run pre-commit run --all-files
