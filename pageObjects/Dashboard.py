from selenium.webdriver.common.by import By


class Dashboard:
    def __init__(self, driver):
        self.driver = driver
    user_registration = (By.ID, "toplevel_page_user-registration")
    add_new = (By.LINK_TEXT, "Add New")

    def enter_user_registration(self):
        return self.driver.find_element(*Dashboard.user_registration)

    def enter_add_new(self):
        return self.driver.find_element(*Dashboard.add_new)
