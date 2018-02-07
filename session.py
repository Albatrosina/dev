from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
