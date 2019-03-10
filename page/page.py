from page.Home_page import HomePage
from page.Login_page import LoginPage
from page.Personal_center_page import PersonalCenterPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home_page(self):
        return HomePage(self.driver)

    @property
    def login_page(self):
        return LoginPage(self.driver)

    @property
    def personal_center_page(self):
        return PersonalCenterPage(self.driver)
