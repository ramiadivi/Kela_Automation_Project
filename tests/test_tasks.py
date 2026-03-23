from pages.dashboard_page import DashboardPage
from playwright.sync_api import expect
import pytest
import time
import utils


def test_cancel_button(page):
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    dashboard.cancel_task("name", "time", "desc")
    validation_text = "nametimeDeletedesc"
    print(f"Validation text: {validation_text}")
    expect(page.get_by_test_id("tasks-list")).not_to_contain_text(validation_text, timeout=2000)
    expect(dashboard.by_test_id(dashboard.TASK_NAME)).to_be_hidden(timeout=2000)
    time.sleep(0.5)


@pytest.mark.parametrize("valid_tasks_list", utils.get_csv_data("test_data\\valid_tasks.csv"))
def test_add_task(page, valid_tasks_list):
    task_name = str(valid_tasks_list[0])
    task_time = str(valid_tasks_list[1])
    task_desc = str(valid_tasks_list[2])
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    dashboard.add_task(task_name, task_time, task_desc)
    validation_text = f"{task_name}{task_time}Delete{task_desc}"
    print(f"Validation text: {validation_text}")
    expect(page.get_by_test_id("tasks-list")).to_contain_text(validation_text, timeout=2000)
    time.sleep(0.5)


def test_delete_task(page):
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    for i in range(5):
        task_name = f"Task {i}"
        task_time = f"2024-06-0{i+1}T12:00:00"
        task_desc = f"Description for Task {i}"
        dashboard.add_task(task_name, task_time, task_desc)
        validation_text = f"{task_name}{task_time}Delete{task_desc}"
        print(f"Validation text: {validation_text}")
        expect(page.get_by_test_id("tasks-list")).to_contain_text(validation_text, timeout=2000)
        # check the delete button is visible and clickable
        page.get_by_test_id("tasks-list").locator("div").filter(has_text=validation_text).get_by_test_id(
         "delete-task-btn").click()
    time.sleep(5)


def test_add_empty_task(page):
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    dashboard.add_task("")
    expect(page.get_by_test_id("task-add-btn")).to_be_visible()
    page.get_by_test_id("dialog-cancel-btn").click()
    time.sleep(0.5)

