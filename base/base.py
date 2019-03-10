import os,time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, loc, timeout=15, poll=1.0):
        """
            定位一个元素
        :param loc: 上传定位的元组，例如（By.ID,id属性值）
        :param timeout: 等待时间
        :param poll: 间隔多长时间搜索依次
        :return: 返回一个元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def search_elements(self, loc,):
        """
            定位一类元素
        :param loc: 上传定位的元组，例如（By.ID,id属性值）
        :param timeout: 等待时间
        :param poll: 间隔多长时间搜索依次
        :return: 返回一类元素
        """
        # return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))
        time.sleep(15)
        return self.driver.find_elements(*loc)

    def click_ele(self, loc):
        """
            点击元素
        :param loc:
        :return:
        """
        self.search_element(loc).click()

    def input_ele(self, loc, text):
        """
            输入文本
        :param loc:
        :param text: 输入的内容
        :return:
        """
        self.search_element(loc).send_keys(text)

    def get_toast(self, message):
        # 获取提示消息
        try:
            xpath = "//*[contains(@text,'{}')]".format(message)
            toast_message = self.search_element((By.XPATH,xpath), timeout=5, poll=0.1)
            return toast_message.text
        except Exception as e:
            return False

    def screen_shot(self,o):
        """
            截图
        :return:
        """
        current_time = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        shot_name = os.getcwd() + os.sep + "screen" + os.sep + current_time+o +".png"
        self.driver.get_screenshot_as_file(shot_name)
