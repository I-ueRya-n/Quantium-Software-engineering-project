#!/bin/bash

# Activate the project virtual environment
source venv/bin/activate

# Execute the test suite
pytest test_app.py

# Capture the exit code of pytest
EXIT_CODE=$?

# Deactivate the virtual environment
deactivate

# Return exit code 0 if all tests passed, or 1 if something went wrong
exit $EXIT_CODE