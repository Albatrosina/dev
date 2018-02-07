from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from model.login import Login
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_to_system(self, login):
        self.app.driver.get("https://crmg-test.rum.devvly.com/user/login?destination=node")
        driver = self.app.driver
        wait = self.app.wait
        wait.until(EC.element_to_be_clickable((By.NAME, "name")))
        # login to the CRMG system
        driver.find_element_by_name("name").send_keys(login.name)
        driver.find_element_by_name("pass").send_keys(login.password)
        driver.find_element_by_name("op").click()

    def logout_from_system(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Log out").click()

    def ensure_logout(self):
        driver = self.app.driver
        if len(driver.find_elements_by_link_text("Log out")) > 0:
            self.logout_from_system()

    def ensure_login(self,login):
        driver = self.app.driver
        if len(driver.find_elements_by_name("op")) > 0:
            self.login_to_system()
