class FillRowHelper:

    def __init__(self, app):
        self.app = app

    def corn(self, fill_row):
        driver = self.app.driver
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