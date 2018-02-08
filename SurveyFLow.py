# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class SurveyFLow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/albatros/mystuff/Autotesting/Dev/chromedriver")
        self.driver.implicitly_wait(30)

    
    def test_survey_f_low(self):
        driver = self.driver
        driver.get("http://test.dev.engagecoach.co.uk/login")
        self.login()
        self.select_survey()
        try:
            self.demo_block()
        except:
            self.pass_survey()
            self.dashboard()

    def pass_survey(self):
        driver = self.driver
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | //form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label | ]]
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr/td[2]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[3]/td[4]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[4]/td[5]/label").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[5]/td[6]/label").click()
        driver.find_element_by_id("button-next").click()
        driver.find_element_by_xpath("//form[@id='questionForm']/div/table/tbody/tr[2]/td[3]/label").click()
        driver.find_element_by_id("button-next").click()

    def dashboard(self):
        driver = self.driver
        driver.find_element_by_link_text("Back to Dashboard").click()

    def demo_block(self):
        driver = self.driver
        Select(driver.find_element_by_name("questionForm[179]")).select_by_visible_text("White/Caucasian")
        Select(driver.find_element_by_name("questionForm[180]")).select_by_visible_text("Female")
        Select(driver.find_element_by_name("questionForm[181]")).select_by_visible_text("Non-managerial")
        Select(driver.find_element_by_name("questionForm[182]")).select_by_visible_text("Pharmaceutical")
        Select(driver.find_element_by_name("questionForm[183]")).select_by_visible_text("18-24 years")
        Select(driver.find_element_by_name("questionForm[184]")).select_by_visible_text("Europe")
        Select(driver.find_element_by_name("questionForm[185]")).select_by_visible_text("No formal education")
        driver.find_element_by_id("button-next").click()

    def select_survey(self):
        # start survey
        driver = self.driver
        driver.find_element_by_link_text("Engage Survey").click()
        driver.find_element_by_link_text("Start").click()

    def login(self):
        # login
        driver = self.driver
        driver.find_element_by_id("loginform-email").clear()
        driver.find_element_by_id("loginform-email").send_keys("dmitry.kadigrabov+9005@requestum.com")
        driver.find_element_by_id("loginform-password").clear()
        driver.find_element_by_id("loginform-password").send_keys("12345")
        el = driver.find_element_by_xpath('//*[@id="r2"]')
        driver.execute_script("arguments[0].click();", el)
        driver.find_element_by_name("login-button").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
