#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：projectManageCase_test.py
@IDE     ：PyCharm 
@Author  ：凯凯西
@Date    ：2021/1/7 11:26 
'''
from PO.pages.projectManager import PA
import pytest

class TestProjectManagerCase:

    def test_project_name_search(self):

        PA.to_page()

        project_name = '内容'
        PA.project_name_input_box().send_keys(project_name)
        PA.search_button_box().click()

        project_name_li = PA.list_of_project_name_box()
        project_ali_name_sli = PA.list_of_project_ali_name()

        for project_name_for in project_name_li:
            as1 = project_name in project_name_for.text
            as2 = project_name in project_ali_name_sli[project_name_li.index(project_name_for)].text

            assert  (as1 or as2)

if __name__ == '__main__':

    pytest.main()

