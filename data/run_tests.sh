# Activate the project virtual environment
source venv/bin/activate

# Execute the test suite
pytest

# Capture the exit code of the pytest command
pytest_exit_code=$?

# Deactivate the virtual environment
deactivate

# Return exit code 0 if all tests passed, or 1 if something went wrong
exit $pytest_exit_code
