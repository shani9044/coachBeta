from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from Utilities.customlogger import logGen
class LoginPage(BasePage):


    login_text = "//div[@class='chakra-stack css-7ojq0j']/form/p[2]"
    work_email_input_xpath = "//input[@id='field-:r1:']"
    password_input_xpath = "//input[@id='field-:r2:']"
    login_button_xpath = "//button[@id='login-form-submit']"
    username_xpath = "//div[@class='css-1ogar5h']"
    toast_message = "//div[@class='chakra-alert__desc css-161kwbg']/div"

    def __init__(self, driver):
        self.logger = logGen.logger()
        super().__init__(driver)

    def get_login_text(self):
        locator = (By.XPATH, self.login_text)
        self.logger.info("*** Verify login page text ***")
        return self.get_text(*locator)

    def set_workemail(self, workemail):
        locator = (By.XPATH, self.work_email_input_xpath)
        self.logger.info("*** Enter Work Mail ***")
        self.send_keys(*locator, workemail)

    def set_password(self, password):
        locator = (By.XPATH, self.password_input_xpath)
        self.logger.info("*** Enter Password ***")
        self.send_keys(*locator, password)

    def click_login(self):
        locator = (By.XPATH, self.login_button_xpath)
        self.logger.info("*** Click on login button ***")
        self.click(*locator)

    def get_username(self):
        locator = (By.XPATH, self.username_xpath)
        self.logger.info("*** Verify username ***")
        return self.get_text(*locator)

    def get_toast_message(self):
        locator = (By.XPATH, self.toast_message)
        self.logger.info("*** Verify error message ***")
        return self.get_text(*locator)