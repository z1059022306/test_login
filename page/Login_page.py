from selenium.webdriver.common.by import By

from base.base import BaseAction


class LoginPage(BaseAction):
    username_loc = By.ID, "username"
    password_loc = By.ID, "password"
    verify_code_loc = By.ID, "verify_code"
    login_submit_loc = By.CLASS_NAME, "J-login-submit"
    prompt_information_loc = By.CLASS_NAME, "layui-layer-title"
    prompt_text_loc = By.CLASS_NAME,"layui-layer-content"



    def input_user(self, text):
        """
            输入用户名
        :param text:
        :return:
        """
        self.input_ele(self.username_loc, text)

    def input_pwd(self, text):
        """
            输入密码
        :param text:
        :return:
        """
        self.input_ele(self.password_loc, text)

    def input_verify_code(self, text):
        """
            输入验证码
        :param text:
        :return:
        """
        self.input_ele(self.verify_code_loc, text)

    def click_login_submit(self):
        """
            点击登录按钮
        :return:
        """
        self.click_ele(self.login_submit_loc)

    def is_exist_prompt(self):
        """
            查找提示框
        :return:
        """
        return self.search_elements(self.prompt_information_loc)

    def get_prompt_text(self):
        """
            获取弹框的提示信息
        :return:
        """
        return self.search_element(self.prompt_text_loc).text
