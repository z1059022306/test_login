from selenium.webdriver.common.by import By

from base.base import BaseAction


class PersonalCenterPage(BaseAction):
    user_info_loc = By.CLASS_NAME, "userinfo"

    def user_info_text(self):
        """
            获取登陆后的用户名
        :return:
        """
        return self.search_element(self.user_info_loc).text
