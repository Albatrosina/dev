from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time


class ActionHelper:

    def __init__(self, app):
        self.app = app

    def switch_to_rpm_tab(self):
        driver = self.app.driver
        self.choose_customer(driver, "Doug Claassen")
        # switch to another account and select the RPM tab
        Select(driver.find_element_by_name("account_numbers")).select_by_value("1")
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[4]/div/ul/li[5]').click()

    def choose_customer(self, driver, name):
        # redirect to the needed customer
        self.app.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Customers")))
        driver.find_element_by_link_text("Customers").click()
        self.app.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"2")))
        driver.find_element_by_link_text("2").click()
        self.app.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, name)))
        driver.find_element_by_link_text(name).click()

    def confirm_targets_row(self):
        # confirm the filled row
        driver = self.app.driver
        driver.find_element_by_id("edit-table-wrapper-table-values-0-fill").click()

    def delete_targets_row(self):
        # delete the filled row
        driver = self.app.driver
        driver.find_element_by_id("edit-table-wrapper-table-values-0-remove").click()

    def delete_fills_row(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="edit-table-wrapper-fills"]/table[2]/tbody/tr[1]/td[16]/a').click()
        self.click_confirm_button()

    def click_confirm_button(self):
        driver = self.app.driver
        driver.find_element_by_id('edit-submit').click()


