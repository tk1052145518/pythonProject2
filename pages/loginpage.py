from PO.myDriverTool.mydriver import Driver
from PO.pages.basepage import username,password
class login:
    def __init__(self):
        self.driver = Driver.getDriver()
    def username_box(self):
        return self.driver.find_element_by_name('username')
    def password_box(self):
        return self.driver.find_element_by_name('password')
    def login_box(self):
        return self.driver.find_element_by_css_selector("button[class='btn btn-lg btn-login btn-block']")

    def logn(self):
        self.username_box().send_keys(username)
        self.password_box().send_keys(password)
        self.login_box().click()

if __name__ == '__main__':

    login().logn()