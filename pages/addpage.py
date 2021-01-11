
from PO.myDriverTool.mydriver import Driver
import time

class Addpage():
    def __init__(self):
        self.driver= Driver.getDriver()

    def menu_box(self):
        return self.driver.find_element_by_css_selector("ul.js-left-nav > li:nth-child(2)")
    def add_box(self):
        return self.driver.find_element_by_css_selector('div > div.pull-right')
    def fabu_box(self):
        return self.driver.find_element_by_css_selector(".col-sm-10 input:nth-child(1)")
    def bieming_box(self):
        return self.driver.find_element_by_css_selector(".col-sm-10 input[name='aliasname']")
    def neirong_box(self):
        return self.driver.find_element_by_css_selector('body.ke-content')
    def queding_box(self):
        return self.driver.find_element_by_css_selector(".col-lg-10 button[class='btn btn-primary']")
    def ele(self):
        return self.driver.find_element_by_css_selector('.ke-edit-iframe')

    def add2(self):
        time.sleep(5)
        self.menu_box().click()
        time.sleep(1)
        self.add_box().click()
        time.sleep(1)
        self.fabu_box().send_keys('发布v')
        self.bieming_box().send_keys('别名')
        time.sleep(1)
        self.driver.switch_to.frame(self.ele())
        self.neirong_box().send_keys('111111')
        self.driver.switch_to.default_content()
        self.queding_box().click()

if __name__ == '__main__':
    Addpage().add2()