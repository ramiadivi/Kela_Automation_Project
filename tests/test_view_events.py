from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage
import time
import utils
import pytest


@pytest.mark.parametrize("event_list", utils.get_csv_data("test_data\\view_events.csv"))
def test_dashboard(page, event_list):
    task_name = str(event_list[0])
    task_time = str(event_list[1])
    task_desc = str(event_list[2])
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    dashboard.add_task(task_name, task_time, task_desc)
    dashboard.view_events()
    assert dashboard.is_event_list_visible()
    expect(page.get_by_test_id("events-list")).to_contain_text(f"Task \"{task_name}\" added at")
    page.get_by_test_id("view-events-btn").click()
    time.sleep(2)

