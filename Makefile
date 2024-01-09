.PHONY: start
start:
	@echo "Starting the application..."
	pipenv run python src/manage.py runserver
