from selenium.webdriver.common.by import By

from base.base import BaseAction


class HomePage(BaseAction):
    login_ele = By.LINK_TEXT, "登录"

    def click_login(self):
        """
            点击登录按钮
        :return:
        """
        self.click_ele(self.login_ele)
