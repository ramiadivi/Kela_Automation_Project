from playwright.sync_api import expect
from pages.login_page import LoginPage
import time
import utils


def test_dashboard(page):
    login = LoginPage(page)
    utils.verify_login(page)
    expect(page.get_by_test_id("dashboard-title")).to_be_visible()
    expect(page.get_by_test_id("add-task-btn")).to_be_visible()
    expect(page.get_by_test_id("add-urgent-event-btn")).to_be_visible()
    expect(page.get_by_test_id("view-events-btn")).to_be_visible()
    expect(page.get_by_test_id("logout-btn")).to_be_visible()
    login.logout()
    time.sleep(0.5)
