#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：projectManager.py
@IDE     ：PyCharm 
@Author  ：凯凯西
@Date    ：2021/1/7 11:35 
'''
from PO.pages.basepage import Basepage
from PO.pages.basepage import Driver
from PO.utils.settings import pages_url_dir
from selenium.webdriver.common.by import By
import time


class ProjectManager(Basepage):

    def to_page(self):
        time.sleep(3)
        self.driver.get(pages_url_dir['ProjectManager'])

    def project_status_select_box(self):

        return self.get_element((By.NAME,'status'))

    def project_name_input_box(self):
        """项目名称搜索输入框"""
        return self.get_element((By.CSS_SELECTOR, "form > input"))

    def search_button_box(self):
        """搜索按钮"""
        return self.get_element((By.CSS_SELECTOR, "button[class=\"btn btn-primary\"]"))

    def create_project_button_box(self):
        """新建项目按钮"""
        return self.get_element((By.CSS_SELECTOR, "a[class=\"btn btn-success\"]"))

    def list_of_project_name_box(self):
        """匹配每一个项目名称，返回元素列表"""
        return self.get_elements((By.CSS_SELECTOR, "tbody > tr > :nth-child(1)"))

    def list_of_project_ali_name(self):
        """匹配每一个项目别名，返回元素列表"""
        return self.get_elements((By.CSS_SELECTOR, "tbody > tr > :nth-child(2)"))

class ProjectManagerAction(ProjectManager):
    pass

PA = ProjectManagerAction()

if __name__ == '__main__':
    PA.to_page()