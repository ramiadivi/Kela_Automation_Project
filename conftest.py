import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
        # browser = p.firefox.launch(
        # browser = p.webkit.launch(
            headless=False, slow_mo=1000,
         )
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def page(browser):
    page = browser.new_page()
    page.goto("http://localhost:5173/")
    yield page
    page.close()
