import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_CHANGES_BUTTON = ("xpath", "//div[h6/text()='Personal Details']//button[@type='submit']")
    ASSERTION_SAVE_BUTTON = ("xpath", "//div[@aria-live='assertive']")
    CHECK_EMPTY_FIELD = ("xpath",
                         "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message "
                         "oxd-input-group__message']")
    SPINNER = ("xpath", "//div[@class='oxd-form-loader']/div[@class='oxd-loading-spinner-container']")

    def change_name(self, new_name):
        self.new_name = new_name
        with allure.step(f"Change name on {new_name}"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
            first_name_field.send_keys(Keys.CONTROL + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            self.wait.until(EC.presence_of_element_located(self.CHECK_EMPTY_FIELD))
            first_name_field.send_keys(new_name)

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_CHANGES_BUTTON)).click()

    @allure.step("Assert pop up in save changed")
    def assert_save(self):
        self.wait.until(EC.invisibility_of_element_located(self.ASSERTION_SAVE_BUTTON))

    @allure.step("Assert changed in field")
    def is_changes_saved(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.new_name))


