# -*- coding: utf-8 -*-
from login import Login
from application import Application
from fill_row import Filling
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_r_p_m_flow(app):
    app.login_to_system(Login(name = "Lead Tiller",password = "Gmtfree123"))
    app.switch_to_rpm_tab()
    app.filling_corn_fields(Filling(bt = "20000",fp = "5", hta = "1",spread = "1", roll = "1",flex = "1",basis = "1",note = "some test note"))


#self.add_line_and_save(driver)

#def add_line_and_save(self, driver):
# Add new line and save tab data
#driver.find_element_by_id("edit-table-wrapper-table-values-0-fill").send_keys(Keys.TAB)
#driver.switch_to_default_content()
#driver.find_element_by_id("edit-add--2").send_keys(Keys.ENTER)
