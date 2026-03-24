from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = "login-username"
    PASSWORD = "login-password"
    LOGIN_BTN = "login-submit"
    LOGOUT_BTN = "logout-btn"
    ERROR = "error-msg"

    def login(self, user, password):
        self.by_test_id(self.USERNAME).fill(user)
        self.by_test_id(self.PASSWORD).fill(password)
        self.by_test_id(self.LOGIN_BTN).click()

    def clear_field(self, field):
        self.by_test_id(self.field).clear()

    def get_error(self):
        return self.by_test_id(self.ERROR).inner_text()

    def logout(self):
        self.by_test_id(self.LOGOUT_BTN).click()
