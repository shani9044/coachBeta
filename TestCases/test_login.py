import time
import pytest
from PageObjects.LoginObjects import LoginPage
from Utilities.config_reader import ConfigReader


class Test_login:

    # todo: Get data from json or excel sheet/google sheet
    data = ConfigReader()
    username = data.get("username")
    password =  data.get("password")
    baseurl = data.get("baseurl")

    def test_invalid_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_workemail(self.username+"test")
        self.lp.set_password(self.password+"test")
        self.lp.click_login()
        loginalert = self.lp.get_toast_message()
        assert loginalert == "User Does Not Exist", "Error occurred while logging in"

    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.set_workemail(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        try:
            username = self.lp.get_username()
            assert username == "John Sinha"
        except:
            assert False, "Login Failed, username not found"
