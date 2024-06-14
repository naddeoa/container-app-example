.PHONY: install run


install:
	poetry install

run:
	poetry run python -m demo.app
