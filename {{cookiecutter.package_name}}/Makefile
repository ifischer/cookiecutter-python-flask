generate-example:  ## Generate code from cookiecutter template
	cookiecutter --overwrite-if-exists --no-input --config-file ./sample_config .
	cd hello_service && \
		make docker-build docker-test && \
		make virtualenv-create virtualenv-test && \
		echo "TEST SUCCESSFUL"

clean:
	rm -rf hello_service/.venv
	rm -rf hello_service/example_project.egg-info
	rm -rf hello_service/.pytest_cache
	find hello_service -name "*.pyc" -exec rm {} \;
