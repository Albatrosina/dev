from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/home/albatros/mystuff/Autotesting/Dev/chromedriver")
        self.wait = WebDriverWait(self.driver,10)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.implicitly_wait(20)

    def filling_corn_fields(self,fill_row):
        driver = self.driver
        # filling "Corn" fields by valid data
        driver.find_element_by_id("tab-bushel-target-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-bushel-target-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-bushel-target-val_0_2018_corn_17617693").send_keys(fill_row.bt)
        driver.find_element_by_id("tab-future-price-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-future-price-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-future-price-val_0_2018_corn_17617693").send_keys(fill_row.fp)
        driver.find_element_by_id("tab-hta-fee-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-hta-fee-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-hta-fee-val_0_2018_corn_17617693").send_keys(fill_row.hta)
        driver.find_element_by_id("tab-spread-gain-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-spread-gain-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-spread-gain-val_0_2018_corn_17617693").send_keys(fill_row.spread)
        driver.find_element_by_id("tab-roll-fee-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-roll-fee-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-roll-fee-val_0_2018_corn_17617693").send_keys(fill_row.roll)
        driver.find_element_by_id("tab-flex-fee-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-flex-fee-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-flex-fee-val_0_2018_corn_17617693").send_keys(fill_row.flex)
        driver.find_element_by_id("tab-basis-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-basis-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-basis-val_0_2018_corn_17617693").send_keys(fill_row.basis)
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").click()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").clear()
        driver.find_element_by_id("tab-notes-val_0_2018_corn_17617693").send_keys(fill_row.note)

    def switch_to_rpm_tab(self):
        driver = self.driver
        self.choose_customer(driver, "Doug Claassen")
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


    def login_to_system(self,login):
        self.driver.get("https://crmg-test.rum.devvly.com/user/login?destination=node")
        driver = self.driver
        wait = self.wait
        wait.until(EC.element_to_be_clickable((By.NAME, "name")))
        # login to the CRMG system
        driver.find_element_by_name("name").send_keys(login.name)
        driver.find_element_by_name("pass").send_keys(login.password)
        driver.find_element_by_name("op").click()

    def destroy(self):
        self.driver.quit()