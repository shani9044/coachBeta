from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=250):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click(self, by, locator):
        element = self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def send_keys(self, by, locator, value):
        element = self.wait.until(EC.visibility_of_element_located((by, locator)))
        element.clear()
        element.send_keys(value)

    def force_send_keys(self, by, locator, value):
        element = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)

    def get_validation_messages(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator))).text

    def get_text(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator))).text

    def wait_for_element_to_disappear(self, by, locator):
        self.wait.until(EC.invisibility_of_element_located((by, locator)))

    def wait_for_element_to_appear(self, by, locator):
        self.wait.until(EC.presence_of_element_located((by, locator)))

    def select_date_from_calendar(self, open_calendar_button_locator, target_year: int, target_month: int, target_day: int):
        self.wait.until(EC.element_to_be_clickable(open_calendar_button_locator)).click()

        month_year_label = (By.CLASS_NAME, "rdp-caption_label")
        next_month_button = (By.NAME, "next-month")

        self.wait.until(EC.visibility_of_element_located(month_year_label))

        while True:
            displayed_month_year = self.driver.find_element(*month_year_label).text
            displayed_date = datetime.strptime(displayed_month_year, "%B %Y")
            if displayed_date.year == target_year and displayed_date.month == target_month:
                break
            self.driver.find_element(*next_month_button).click()
            self.wait.until(EC.visibility_of_element_located(month_year_label))

        day_locator = (By.XPATH, f"//button[@name='day' and text()='{target_day}' and not(@disabled)]")
        self.wait.until(EC.element_to_be_clickable(day_locator)).click()