# elastiq_assessment

# Overview
This project automates a test related to the Selenium Playground Table . 
It validates that when searching for "New York" in the search box, the filtered results and total table entries match the expected counts.

# Prerequisites
1.	Python: Ensure Python 3.8 or above is installed on your system.
2.	Google Chrome: Install Google Chrome (version 131.0). 
3.	Python Packages: Install Python packages mentioned in the requirements.txt file using pip.

# Setup Instructions
1.	Clone or download this repository to your local machine.
2.	Install dependencies by running:
     pip install -r requirements.txt

# Running the Test
1.	Open a terminal and navigate to the project directory.
2.	Execute the test script with Pytest:
     pytest -vrA --html=html_report tests/qa_selenium_test.py
3.	Observe the test results in the terminal. If the test passes, it confirms the search functionality is working as expected.

# Test Workflow
1.	The test navigates to the table-sort-search-demo page.
2.	It locates the search input box and enters the query "New York".
3.	The script validates that the visible search results show 5 entries out of 24 total entries.

# Notes
1.	Ensure a stable internet connection when running the test to load the web page properly.

# Troubleshooting
1.	Browser or Driver Issues: Ensure ChromeDriver matches the installed Chrome version.
2.	Timeouts: If the test fails due to slow loading, try again when network is stable.
3.	Dependency Issues: Ensure all required Python packages are installed correctly.
