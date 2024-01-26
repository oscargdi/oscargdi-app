#!/usr/bin/env bash

echo "Running postCreateCommand.sh"

pipenv install --dev
pipenv run pre-commit install
