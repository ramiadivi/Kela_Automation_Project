from pages.base_page import BasePage


class DashboardPage(BasePage):

    # ---------- TASK   ----------
    ADD_TASK_BTN = "add-task-btn"
    TASK_NAME = "task-name-input"
    TASK_TIME = "task-time-input"
    TASK_DESC = "task-description-input"
    SAVE_TASK = "task-add-btn"
    CANCEL_TASK = "dialog-cancel-btn"

    def add_task(self, task_name, task_time="", task_desc=""):
        self.by_test_id(self.ADD_TASK_BTN).click()
        self.by_test_id(self.TASK_NAME).fill(task_name)
        self.by_test_id(self.TASK_TIME).fill(task_time)
        self.by_test_id(self.TASK_DESC).fill(task_desc)
        self.by_test_id(self.SAVE_TASK).click()

    def cancel_task(self, task_name, task_time="", task_desc=""):
        self.by_test_id(self.ADD_TASK_BTN).click()
        self.by_test_id(self.TASK_NAME).fill(task_name)
        self.by_test_id(self.TASK_TIME).fill(task_time)
        self.by_test_id(self.TASK_DESC).fill(task_desc)
        self.by_test_id(self.CANCEL_TASK).click()

    # ---------- EVENT   ----------
    ADD_EVENT_BTN = "add-urgent-event-btn"
    EVENT_TYPE = "urgent-event-type-select"
    EVENT_DATE = "urgent-event-time-input"
    EVENT_DESC = "urgent-event-description-input"
    EVENT_URGENT = "urgent-event-toggle"
    SAVE_EVENT = "urgent-event-add-btn"
    CANCEL_URGENT_BTN = "urgent-dialog-cancel-btn"

    def add_urgent_event(self, event_type="attack", date="", desc="", urgent=False):
        self.by_test_id(self.ADD_EVENT_BTN).click()
        self.by_test_id(self.EVENT_TYPE).select_option(event_type)
        self.by_test_id(self.EVENT_DATE).fill(date)
        self.by_test_id(self.EVENT_DESC).fill(desc)
        if urgent:
            self.by_test_id(self.EVENT_URGENT).check()
        self.by_test_id(self.SAVE_EVENT).click()

    def cancel_urgent_event(self, event_type="attack", date="", desc="", urgent=False):
        self.by_test_id(self.ADD_EVENT_BTN).click()
        self.by_test_id(self.EVENT_TYPE).select_option(event_type)
        self.by_test_id(self.EVENT_DATE).fill(date)
        self.by_test_id(self.EVENT_DESC).fill(desc)
        if urgent:
            self.by_test_id(self.EVENT_URGENT).check()
        self.by_test_id(self.CANCEL_URGENT_BTN).click()

    # ---------- VIEW EVENT   ----------
    VIEW_EVENTS_BTN = "view-events-btn"
    EVENT_LIST = "events-section"

    def view_events(self):
        self.by_test_id(self.VIEW_EVENTS_BTN).click()

    def is_event_list_visible(self):
        return self.by_test_id(self.EVENT_LIST).is_visible()