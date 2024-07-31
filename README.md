# chatgpt_test
Test_By_Man: ChatGPT Automation Testing Framework
This project is a robust test automation suite for the ChatGPT application using Pytest and Playwright. It provides a structured approach to ensure the functionality of the application is working as expected through various fixtures and test cases.

# Setup
Prerequisites

Python 3.10 or higher
pip (Python package installer)

Create a virtual environment:
python -m venv .venv
Activate the virtual environment:

# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install the required packages:
pip3 install playtest
pip3 install playwright
pip3 install selenium
pip3 install lorem_text

# Install Playwright browsers:
playwright install

# Configuration
Update the config/config.py file with necessary configurations such as logging settings, URLs, and other environment-specific variables.
# Running Tests
# To run all tests:
	pytest
# To run a specific test file:
	pytest tests/test_chat_gpt_upload.py
# To run tests with detailed output:
	pytest -v

# Fixtures
The conftest.py file includes the following fixtures:

browser: Initializes the Playwright browser.
page: Creates a new page in the browser and sets up video recording for the test.

# Logging
Logging is configured in utils/logger.py. Adjust the logger settings in config/config.py as needed.
Troubleshooting

Ensure all file paths are correct and files exist.
Check the logs for detailed error messages.
Verify that the virtual environment is activated before running tests.
Make sure all dependencies are installed and up to date.

# Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
