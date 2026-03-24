import pytest
from playwright.sync_api import sync_playwright

"""
This conftest.py file sets up the Playwright browser and page 
fixtures for the test suite. 
The browser fixture launches a Chromium browser instance 
(you can switch to Firefox or WebKit if needed) and yields it for 
use in tests. 
The page fixture creates a new page, navigates to the 
application's URL, and yields it for use in tests. After the tests
are done, both the page and browser are closed to clean up 
 resources.
"""


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
        # browser = p.firefox.launch(
        # browser = p.webkit.launch(
            headless=False, slow_mo=200,
         )
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    page = browser.new_page()
    page.goto("http://localhost:5173/")
    yield page
    page.close()
