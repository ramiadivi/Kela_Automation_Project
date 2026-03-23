class BasePage:
    def __init__(self, page):
        self.page = page

    def by_test_id(self, test_id):
        return self.page.get_by_test_id(test_id)

