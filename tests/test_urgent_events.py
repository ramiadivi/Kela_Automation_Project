from pages.dashboard_page import DashboardPage
from playwright.sync_api import expect
import pytest
from datetime import datetime
import time
import utils


"""
This test verifies that a user can successfully cancel the addition 
of an urgent event and that the event does not appear in the 
urgent events list.
It checks that the cancel button works correctly and that the 
event is not added to the list after cancellation.
"""


def test_urgent_cancel_button(page):
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    event_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    dashboard.cancel_urgent_event("attack", event_time, "desc", urgent=True)
    expect(page.get_by_test_id("tasks-list")).not_to_contain_text(event_time, timeout=2000)
    expect(dashboard.by_test_id(dashboard.EVENT_DATE)).to_be_hidden(timeout=2000)
    time.sleep(0.5)


"""
This test verifies that a user can successfully add an urgent event 
with valid details and that the event appears in the urgent 
events list.
It uses parameterization to test multiple sets of valid urgent 
event details from a CSV file.
"""


@pytest.mark.parametrize("valid_urgent_events_list", utils.get_csv_data("test_data\\valid_urgent_events.csv"))
def test_add_urgent_event(page, valid_urgent_events_list):
    event_type = str(valid_urgent_events_list[0])
    event_time = str(valid_urgent_events_list[1])
    event_desc = str(valid_urgent_events_list[2])
    event_urgency = str(valid_urgent_events_list[3])
    urgency = utils.str_to_bool(event_urgency)
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    dashboard.add_urgent_event(event_type, event_time, event_desc, urgent=urgency)
    converted_event = utils.event_type_conversion(event_type)
    validation_text = f"{converted_event}{event_time}Delete{event_desc}"
    print(f"Validation text: {validation_text}")
    expect(page.get_by_test_id("urgent-events-section")).to_contain_text(validation_text, timeout=2000)
    # check the delete button is visible and clickable
    page.get_by_test_id("urgent-events-list").locator("div").filter(has_text=validation_text).get_by_test_id(
        "delete-urgent-event-btn").click()
    time.sleep(0.5)


"""
This test verifies that a user cannot add an urgent event with 
empty details and that the urgent event is not added to the
 urgent events list.
It checks that the add button remains visible and that the urgent 
event is not added to the list after attempting to add an event 
with empty details.   
"""


def test_add_empty_events(page):
    utils.verify_login(page)
    dashboard = DashboardPage(page)
    dashboard.add_urgent_event("")
    expect(page.get_by_test_id("urgent-event-add-btn")).to_be_visible()
    page.get_by_test_id("urgent-dialog-cancel-btn").click()
    time.sleep(0.5)
