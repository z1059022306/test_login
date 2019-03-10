import time, os

import pytest

from base.init_driver import init_driver
from base.read_data import Op_Data
from page.page import Page


def get_data():
    data_list = []
    data = Op_Data("login.yaml").read_yaml().get("Login_data")

    for i in data:
        for o in i.keys():
            data_list.append((o, i.get(o).get("username"),
                              i.get(o).get("passwd"),
                              i.get(o).get("yanzheng"),
                              i.get(o).get("expect_message1")))
    return data_list


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):

        time.sleep(10)
        self.driver.quit()

    @pytest.mark.parametrize('o,a, b, c,d', get_data())
    def test_login(self, o, a, b, c, d):
        # 点击登录按钮
        self.page.home_page.click_login()
        self.page.login_page.input_user(a)
        self.page.login_page.input_pwd(b)
        self.page.login_page.input_verify_code(c)
        self.page.login_page.click_login_submit()
        ll = self.page.login_page.is_exist_prompt()
        if len(ll) == 0:
            info = self.page.personal_center_page.user_info_text()
            try:
                assert info in d

            except:
                self.page.personal_center_page.screen_shot(o)
        else:
            b = self.page.login_page.get_prompt_text()
            try:
                assert d in b

            except:
                self.page.personal_center_page.screen_shot(o)
