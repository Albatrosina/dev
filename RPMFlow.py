# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class RPMFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver,20)
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_r_p_m_flow(self):
        driver = self.driver
        self.get_url(driver)
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.NAME, "edit-name")))
        self.login_to_system(driver,name = "Lead Tiller",password = "Gmtfree123")
        self.choose_customer(driver, "Doug Claassen")
        driver.find_element_by_css_selector("li.horizontal-tab-button.horizontal-tab-button-4.last.ajax-tab-loaded > a > strong").click()
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
        driver.find_element_by_xpath("//div[@id='edit-table-wrapper--2']/table[2]/tbody/tr[2]/td[10]").click()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").send_keys("test note")

    def choose_customer(self, driver, name):
        # redirect to the needed customer
        driver.find_element_by_link_text("Customers").click()
        driver.find_element_by_link_text("2").click()
        driver.find_element_by_link_text(name).click()

    def get_url(self, driver):
        driver.get("https://crmg-test.rum.devvly.com/user/login?destination=node")

    def login_to_system(self, driver,name,password):
        # login to the CRMG system
        driver.find_element_by_name("edit-name").click()
        driver.find_element_by_name("edit-name").send_keys(name)
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
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
