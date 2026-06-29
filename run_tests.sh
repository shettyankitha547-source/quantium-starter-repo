#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run tests
pytest -v

# Capture exit code
exit_code=$?

# Return success/failure to CI
if [ $exit_code -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Tests failed!"
  exit 1
fi