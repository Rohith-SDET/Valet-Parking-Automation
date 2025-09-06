Parking Cost Calculator – UI Automation (Python, Selenium, Pytest)

Description:
This project contains end-to-end UI automation for the Parking Cost Calculator demo app. 
Automation uses Python, Selenium WebDriver and Pytest, following Page Object Model (POM) principles. 
Tests cover various parking types including Valet, Short-Term, Long-Term Garage, Long-Term Surface, and Economy.

App Under Test:
- Parking Cost Calculator (Practice ExpandTesting)

Features:
- Parametrized tests for multiple parking types and durations
- Page Object Model: pages/parking_page.py encapsulates locators and actions
- HTML reports for test execution results

Project Structure:
- pages/parking_page.py          -> POM for calculator page
- tests/test_valet_POM.py        -> Recommended POM-based test suite
- tests/test_valet.py            -> Direct WebDriver example
- reports/                       -> HTML reports output
- requirements.txt               -> Python dependencies
- README.md                      -> Project documentation

Prerequisites:
- Python 3.10+
- Google Chrome installed
- Matching ChromeDriver on PATH
  (Recommended: use webdriver-manager for automatic driver management)

Setup:
1. Create virtual environment
   Windows:
     python -m venv .venv
     .venv\Scripts\activate
   macOS/Linux:
     python -m venv .venv
     source .venv/bin/activate

2. Install dependencies
   pip install selenium pytest pytest-html

Running Tests:
- Run all tests: pytest -q
- Run with HTML report: pytest -q --html=reports/report.html --self-contained-html
- Run specific test file: pytest -q tests/test_valet_POM.py

Notes:
- Tests fill dates via JavaScript for reliability
- Implicit waits are used; explicit waits can replace sleeps
- Extend tests with assertions comparing displayed cost to expected calculations
- Parametrization allows testing multiple parking types and durations


