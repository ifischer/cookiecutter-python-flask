.PHONY: help
.DEFAULT_GOAL := help
CONTAINER  = hello_service_container
VIRTUALENV_DIR = .venv
LOCAL_PORT = 5001

help:
	# Print help by extracting ##-comments per target
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

docker-clean:
	docker stop --rm $(CONTAINER)

docker-build:  ## Build Docker container
	docker build -t $(CONTAINER) .

docker-run:  ## Run Docker container
	docker run -v $$(pwd):/code -p $(LOCAL_PORT):5000 $(CONTAINER)

docker-shell:  ## Run Docker shell
	docker run -v $$(pwd):/code -it --rm $(CONTAINER) bash

docker-test:
	docker run --rm -i -t $(CONTAINER) pytest

docker-ipython:
	docker run -v $$(pwd):/code $(CONTAINER) ipython


virtualenv-create:  ## Create virtualenv
	virtualenv --python=$$(which python3.7) $(VIRTUALENV_DIR)
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements.txt
	$(VIRTUALENV_DIR)/bin/pip3 install -r requirements-dev.txt
	$(VIRTUALENV_DIR)/bin/pip3 install -e .
	@echo "Activate virtualenv:\n. $(VIRTUALENV_DIR)/bin/activate"

virtualenv-test:
	$(VIRTUALENV_DIR)/bin/pytest

virtualenv-run:
	FLASK_APP=hello_service/hello_service.py $(VIRTUALENV_DIR)/bin/flask run --port $(LOCAL_PORT)


lint:  ## Run linter (Flake8, isort)
	docker run --rm -it $(CONTAINER) pytest --flake8
	docker run --rm -it $(CONTAINER) pytest --isort
