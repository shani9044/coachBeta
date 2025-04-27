from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from Utilities.customlogger import logGen


class CampaignObjects(BasePage):

    campaign_menu = "//span[text()='Campaigns']"
    add_campaign_button = "//button[text()='Add Campaign']"
    add_campaign_title = "//input[@name='Campaign Title']"
    add_campaign_description = "//textarea[@name='Description']"
    click_add_campaign_start_date_button = "//*[@id='popover-trigger-custom-day-picker-start-date']"
    text_month_year_label = "//*[@class='rdp-caption_label']"
    next_month_button = "//button[@name='next-month']"
    day_selection_button = "//button[@name='day' and text()='{day}' and not(@disabled)]"
    click_add_campaign_end_date_button = "//*[@id='popover-trigger-custom-day-picker-end-date']"
    select_campaign_reward = "//*[@id='react-select-2-input']"
    select_campaign_partner_program = "//*[@id='react-select-3-input']"
    select_partner_type = "//*[@id='react-select-4-input']"
    select_partner_group = "//*[@id='react-select-5-input']"
    select_partner_tier = "//*[@id='react-select-6-input']"
    select_partner = "//*[@id='react-select-7-input']"
    add_goal_title = "//input[@name='Goal Title']"
    select_action = "//*[@id='react-select-8-input']"
    add_destination_link = "//input[@name='Destination Link to Track']"
    save_campaign_button = "//*[@id='save-campaign']"
    toast_message = "(//div[@class='chakra-alert__desc css-161kwbg'])[1]"


    def __init__(self, driver):
        self.logger = logGen.logger()
        self.logger.info("*** Initialize Campaign Objects ***")
        super().__init__(driver)

    def clickcampaignmenu(self):
        locator = (By.XPATH, self.campaign_menu)
        self.logger.info("*** Scroll to and click on campaign menu ***")
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click(*locator)
        
    def clickonaddcampaign(self):
        locator = (By.XPATH, self.add_campaign_button)
        self.logger.info("*** Click on add campaign button ***")
        self.click(*locator)
        
    def addcampaigntitle(self, title):
        locator = (By.XPATH, self.add_campaign_title)
        self.logger.info("*** Add campaign title ***")
        self.send_keys(*locator, title)
    
    def addcampaigndescription(self, description):
        locator = (By.XPATH, self.add_campaign_description)
        self.logger.info("*** Add campaign description ***")
        self.send_keys(*locator, description)

    def addcampaignstartdate(self, month: int, year: int, day: int):
        self.select_date_from_calendar(
            (By.XPATH, self.click_add_campaign_start_date_button),
            target_year=year,
            target_month=month,
            target_day=day)

    def addcampaignenddate(self, month: int, year: int, day: int):
        (self.select_date_from_calendar
        (
            (By.XPATH, self.click_add_campaign_end_date_button),
            target_year=year,
            target_month=month,
            target_day=day
        ))

    def selectcampaignreward(self, reward):
        locator = (By.XPATH, self.select_campaign_reward)
        self.send_keys(*locator, reward)
        locator = (By.XPATH, f"//*[text()='{reward}']")
        self.click(*locator)
        self.logger.info("*** Selected campaign reward ***")

    def selectcampaignpartnerprogram(self, partner_program):
        locator = (By.XPATH, self.select_campaign_partner_program)
        self.send_keys(*locator, partner_program)
        locator = (By.XPATH, f"//*[text()='{partner_program}']")
        self.click(*locator)
        self.logger.info("*** Selected campaign partner program ***")

    def selectpartnertype(self, partner_type):
        locator = (By.XPATH, self.select_partner_type)
        self.send_keys(*locator, partner_type)
        locator = (By.XPATH, f"//*[text()='{partner_type}']")
        self.click(*locator)
        self.logger.info("*** Selected partner type ***")

    def selectpartnergroup(self, partner_group):
        locator = (By.XPATH, self.select_partner_group)
        self.send_keys(*locator, partner_group)
        locator = (By.XPATH, f"//*[text()='{partner_group}']")
        self.click(*locator)
        self.logger.info("*** Selected partner group ***")

    def selectpartnertier(self, partner_tier):
        locator = (By.XPATH, self.select_partner_tier)
        self.logger.info("*** Select partner tier ***")
        self.send_keys(*locator, partner_tier)
        locator = (By.XPATH, f"//*[text()='{partner_tier}']")
        self.click(*locator)

    def selectpartner(self, partner):
        locator = (By.XPATH, self.select_partner)
        self.logger.info("*** Select partner ***")
        self.send_keys(*locator, partner)
        locator = (By.XPATH, f"//*[text()='{partner}']")
        self.click(*locator)

    def addgoaltitle(self, goaltitle):
        locator = (By.XPATH, self.add_goal_title)
        self.send_keys(*locator, goaltitle)

    def selectaction(self, action):
        locator = (By.XPATH, self.select_action)
        self.logger.info("*** Select action ***")
        self.send_keys(*locator, action)
        locator = (By.XPATH, f"//*[text()='{action}']")
        self.click(*locator)

    def adddestinationlink(self, destination_link):
        locator = (By.XPATH, self.add_destination_link)
        self.logger.info("*** Add destination link ***")
        self.send_keys(*locator, destination_link)

    def clicksavecampaign(self):
        locator = (By.XPATH, self.save_campaign_button)
        self.logger.info("*** Click save campaign button ***")
        self.click(*locator)


    def get_toast_message(self):
        locator = (By.XPATH, self.toast_message)
        self.logger.info("*** Verify error message ***")
        return self.get_text(*locator)