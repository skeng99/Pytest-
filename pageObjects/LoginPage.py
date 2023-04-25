from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "user_login")
    password = (By.ID, "user_pass")
    submit = (By.XPATH, "//input[@id='wp-submit']")

    def enter_username(self):
        return self.driver.find_element(*LoginPage.username)

    def enter_password(self):
        return self.driver.find_element(*LoginPage.password)

    def click_login_button(self):
        return self.driver.find_element(*LoginPage.submit)


