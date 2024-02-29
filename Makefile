.PHONY: start
start:
	@echo "Starting the application..."
	pipenv run python src/manage.py runserver

.PHONY: dramatiq
dramatiq:
	@echo "Starting the worker..."
	PYTHONPATH=src pipenv run python src/manage.py rundramatiq --reload

.PHONY: pre-commit
pre-commit:
	@echo "Running pre-commit hooks..."
	pipenv run pre-commit run --all-files
