from PO.myDriverTool.mydriver import Driver
from utils.settings import time_out,poll_time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Basepage:

    def __init__(self):
            self.driver = Driver.getDriver('Chrome')

    def get_element(self,locator):
        """
                显示等待，查找元素
                :param locator: 要求传入的参数是一个元组，表示元素定位方法和表达式
                :return: 单个的元素对象
        """
        WebDriverWait(
            driver=self.driver,
            timeout=time_out,
            poll_frequency=poll_time).until(
            EC.visibility_of_element_located(locator)
        )

        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """
        显示等待，查找元素
        :param locator: 要求传入的参数是一个元组，表示元素定位方法和表达式
        :return: 元素列表
        """
        WebDriverWait(
            driver=self.driver,
            timeout=time_out,
            poll_frequency=poll_time).until(
            EC.visibility_of_element_located(locator)
        )

        return self.driver.find_elements(*locator)

        
