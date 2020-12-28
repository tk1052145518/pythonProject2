from selenium import webdriver
from PO.settings import username,password,url

class Driver:
    driver = None
    @classmethod
    def getDriver(cls,browser_name='Chrome'):
        if cls.driver is None:
            if browser_name=='Chrome':
                cls.driver = webdriver.Chrome()
            elif browser_name=='FirFox':
                cls.driver = webdriver.Firefox()

            cls.driver.maximize_window()
            cls.driver.get(url)
            cls.login()
        return cls.driver

    @classmethod
    def login(cls):
        cls.driver.find_element_by_name('username').send_keys(username)
        cls.driver.find_element_by_name('password').send_keys(password)
        cls.driver.find_element_by_css_selector("button[class='btn btn-lg btn-login btn-block']").click()


if __name__ == '__main__':
    Driver.getDriver()
