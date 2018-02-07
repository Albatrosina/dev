from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from fixture.session import SessionHelper
from fixture.fill_row import FillRowHelper
from fixture.actions import ActionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/home/albatros/mystuff/Autotesting/Dev/chromedriver")
        self.wait = WebDriverWait(self.driver,10)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.fill = FillRowHelper(self)
        self.action = ActionHelper(self)

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def destroy(self):
        self.driver.quit()