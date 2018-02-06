# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest,time


class RPMFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/albatros/mystuff/Autotesting/Dev/chromedriver")
        self.wait = WebDriverWait(self.driver,40)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.implicitly_wait(20)

    def test_r_p_m_flow(self):
        driver = self.driver
        self.get_url(driver)
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.NAME, "name")))
        self.login_to_system(driver,name = "Lead Tiller",password = "Gmtfree123")
        self.choose_customer(driver, "Doug Claassen")
        self.switch_to_rpm_tab(driver)
        self.filling_corn_fields(driver)
        self.add_line_and_save(driver)

    def add_line_and_save(self, driver):
        # Add new line and save tab data
        driver.find_element_by_id("edit-table-wrapper-table-values-0-fill").send_keys(Keys.TAB)
        driver.switch_to_default_content()
        driver.find_element_by_id("edit-add--2").send_keys(Keys.ENTER)


    def filling_corn_fields(self, driver):
        # filling "Corn" fields by valid data
        driver.find_element_by_id("tab-bushel-target-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-bushel-target-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-bushel-target-val_0_2018_corn_17617693").send_keys("20000")
        driver.find_element_by_id("tab-future-price-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-future-price-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-future-price-val_0_2018_corn_17617693").send_keys("5")
        driver.find_element_by_id("tab-hta-fee-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-hta-fee-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-hta-fee-val_0_2018_corn_17617693").send_keys("1")
        driver.find_element_by_id("tab-spread-gain-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-spread-gain-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-spread-gain-val_0_2018_corn_17617693").send_keys("1")
        driver.find_element_by_id("tab-roll-fee-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-roll-fee-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-roll-fee-val_0_2018_corn_17617693").send_keys("1")
        driver.find_element_by_id("tab-flex-fee-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-flex-fee-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-flex-fee-val_0_2018_corn_17617693").send_keys("1")
        driver.find_element_by_id("tab-basis-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-basis-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-basis-val_0_2018_corn_17617693").send_keys("1")
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").send_keys("test note")

    def switch_to_rpm_tab(self, driver):
        # switch to another account and select the RPM tab
        Select(driver.find_element_by_name("account_numbers")).select_by_value("1")
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="block-system-main"]/div/div[4]/div/ul/li[5]').click()

    def choose_customer(self, driver, name):
        # redirect to the needed customer
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Customers")))
        driver.find_element_by_link_text("Customers").click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"2")))
        driver.find_element_by_link_text("2").click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, name)))
        driver.find_element_by_link_text(name).click()

    def get_url(self, driver):
        driver.get("https://crmg-test.rum.devvly.com/user/login?destination=node")

    def login_to_system(self, driver,name,password):
        # login to the CRMG system
        driver.find_element_by_name("name").send_keys(name)
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_name("op").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    #def tearDown(self):
        #self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
