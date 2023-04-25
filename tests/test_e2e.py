import time

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select

from pageObjects.Dashboard import Dashboard
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_dashboard(self):
        log = self.getLogger()
        dash_board = Dashboard(self.driver)
        dash_board.enter_user_registration().click()
        dash_board.enter_add_new().click()
        log.info("welcome to form builder page")
        self.driver.implicitly_wait(5)

    def test_formbuilder(self):
        log = self.getLogger()
        actions = ActionChains(self.driver)
        hover = self.driver.find_element(By.LINK_TEXT, "Start From Scratch")
        actions.move_to_element(hover).perform()
        print("Done Mouse Hover on Start From Scratch")
        log.info("Done mouse hover on Start From Scratch")
        self.driver.find_element(By.LINK_TEXT, "Start From Scratch").click()
        print(self.driver.find_element(By.XPATH, "//span[@class='user-registration-swal2-modal__title']").text)
        # self.driver.find_element(By.CLASS_NAME, "swal2-input").send_keys("Register form")
        self.driver.find_element(By.CLASS_NAME, "swal2-input").send_keys("Register form")
        self.driver.find_element(By.CLASS_NAME, "user-registration-template-continue").click()
        self.driver.find_element(By.CSS_SELECTOR, ".jconfirm-closeIcon").click()
        log.info("welcome to form drag and drop")

    def test_drag_and_drop(self):
        actions = ActionChains(self.driver)
        log = self.getLogger()
        # target1 = self.driver.find_element(By.XPATH, "(//div[@class='ur-grid-list-item ui-sortable'])[1]")
        target1 = self.driver.find_element(By.XPATH, "(//div[@class='ur-grid-list-item ui-sortable'])[")
        target2 = self.driver.find_element(By.XPATH, "(//div[@class='ur-grid-list-item ui-sortable'])[2]")

        print(self.driver.find_element(By.XPATH, "(//li[@id='user_registration_user_confirm_email_list '])[1]").text)
        source1 = self.driver.find_element(By.XPATH, "(//li[@id='user_registration_user_confirm_email_list '])[1]")
        actions.move_to_element(source1).perform()
        # time.sleep(5)
        actions.move_to_element(target1).perform()
        actions.drag_and_drop(source1, target1).perform()

        print(self.driver.find_element(By.XPATH, "(//li[@id='user_registration_nickname_list '])[1]").text)
        source2 = self.driver.find_element(By.XPATH, "(//li[@id='user_registration_nickname_list '])[1]")
        actions.move_to_element(source2).perform()
        # time.sleep(5)
        actions.move_to_element(target2).perform()
        actions.drag_and_drop(source2, target2).perform()

        print(self.driver.find_element(By.XPATH, "(//li[@id='user_registration_user_url_list '])[1]").text)
        source3 = self.driver.find_element(By.XPATH, "(//li[@id='user_registration_user_url_list '])[1]")
        actions.move_to_element(source3).perform()
        # time.sleep(5)
        actions.move_to_element(target1).perform()
        actions.drag_and_drop(source3, target1).perform()

        print(self.driver.find_element(By.XPATH, "(//li[@id='user_registration_first_name_list '])[1]").text)
        source4 = self.driver.find_element(By.XPATH, "(//li[@id='user_registration_first_name_list '])[1]")
        actions.move_to_element(source4).perform()
        # time.sleep(5)
        actions.move_to_element(target2).perform()
        actions.drag_and_drop(source4, target2).perform()

        print(self.driver.find_element(By.XPATH, "(//li[@id='user_registration_last_name_list '])[1]").text)
        source5 = self.driver.find_element(By.XPATH, "(//li[@id='user_registration_last_name_list '])[1]")
        actions.move_to_element(source5).perform()
        # time.sleep(5)
        actions.move_to_element(target1).perform()
        actions.drag_and_drop(source5, target1).perform()
        time.sleep(5)

        self.driver.find_element(By.NAME, "save_form").click()

        self.driver.find_element(By.LINK_TEXT, "Preview").click()

        time.sleep(5)

        # driver.switch_to.new_window(WindowType.WINDOW)

        windows = self.driver.window_handles
        parent_id = windows[0]
        child_id = windows[1]
        # child_id2 = windows[2]
        #
        self.driver.switch_to.window(child_id)
        time.sleep(5)
        str_url = self.driver.current_url
        print("Current URL is: " + str_url)
        #
        # driver.switch_to.window(child_id2)
        #
        faker = Faker()
        password = faker.password()
        email = faker.email()
        username = faker.user_name()
        lastname = faker.last_name()
        firstname = faker.first_name()
        url = faker.url()

        self.driver.find_element(By.ID, "first_name").send_keys(firstname)
        self.driver.find_element(By.ID, "last_name").send_keys(lastname)
        self.driver.find_element(By.ID, "user_login").send_keys(username)
        self.driver.find_element(By.ID, "user_pass").send_keys(password)
        self.driver.find_element(By.ID, "user_url").send_keys(url)
        self.driver.find_element(By.ID, "user_confirm_password").send_keys(password)
        self.driver.find_element(By.ID, "user_email").send_keys(email)
        self.driver.find_element(By.ID, "nickname").send_keys(username)
        self.driver.find_element(By.NAME, "user_confirm_email").send_keys(email)

        time.sleep(5)

        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        print(self.driver.find_element(By.CSS_SELECTOR, "div[id='ur-submit-message-node'] ul").text)

        time.sleep(5)

        self.driver.switch_to.window(parent_id)
        self.driver.find_element(By.LINK_TEXT, "Form Settings").click()

        dropdown = Select(self.driver.find_element(By.ID, "user_registration_form_setting_login_options"))
        # dropdown.select_by_visible_text("")
        dropdown.select_by_index(3)

        self.driver.find_element(By.NAME, "save_form").click()

        self.driver.find_element(By.LINK_TEXT, "Preview").click()


        firefox_options = Options()
        firefox_options.add_argument("-private")
        driver = webdriver.Firefox(options=firefox_options)
        # print(get_url)
        driver.get("http://user-registration-automation.local/register/")
        driver.maximize_window()

        password1 = faker.password()
        username1 = faker.user_name()
        email1 = faker.user_name() + "@getnada.com"
        lastname1 = faker.last_name()
        firstname1 = faker.first_name()
        url1 = faker.url()

        var = email1.split("@")
        print(var[0])
        driver.find_element(By.ID, "first_name").send_keys(firstname1)
        driver.find_element(By.ID, "last_name").send_keys(lastname1)
        driver.find_element(By.ID, "user_login").send_keys(username1)
        driver.find_element(By.ID, "user_pass").send_keys(password1)
        driver.find_element(By.ID, "user_url").send_keys(url1)
        driver.find_element(By.ID, "user_confirm_password").send_keys(password1)
        driver.find_element(By.ID, "user_email").send_keys(email1)
        driver.find_element(By.ID, "nickname").send_keys(username1)
        driver.find_element(By.NAME, "user_confirm_email").send_keys(email1)
        time.sleep(10)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        driver.get("https://getnada.com/")
        driver.find_element(By.XPATH, "//button[contains(text(),'Add inboxe')]").click()
        time.sleep(5)
        driver.find_element(By.ID, "grid-first-name").clear()
        time.sleep(5)
        driver.find_element(By.ID, "grid-first-name").send_keys(var[0])

        dropdown1 = Select(driver.find_element(By.TAG_NAME, "select"))
        dropdown1.select_by_visible_text("@getnada.com")
        driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()


        verify = driver.find_element(By.XPATH, "//a[contains(text(),'User Registration Automation')]")
        driver.execute_script("arguments[0].click();", verify)

        time.sleep(4)
        # iframe = driver.find_element(By.ID, "the_message_iframe")
        driver.switch_to.frame("the_message_iframe")

        driver.find_element(By.XPATH, "//a[normalize-space()='Click here']").click()
        print(driver.find_element(By.XPATH, "//a[normalize-space()='Click here']").text)
        time.sleep(5)

        windows = driver.window_handles
        parent_id1 = windows[0]
        child_id2 = windows[1]
        driver.switch_to.window(child_id2)

        driver.find_element(By.ID, "username").send_keys(email1)
        driver.find_element(By.ID, "password").send_keys(password1)
        driver.find_element(By.XPATH, "//input[@name='login']").click()




