import time
from PageObjects.CampaignObjects import CampaignObjects
from Utilities.datagenerator import RandomDataGenerator


class Test_campaign:

    data = RandomDataGenerator()
    title = data.random_title(20)
    description = data.random_sentence(20)

    def test_addnewcampaign(self, setup, login_fixture):
        self.driver = setup
        self.cp = CampaignObjects(self.driver)
        self.cp.clickcampaignmenu()
        self.cp.clickonaddcampaign()
        self.cp.addcampaigntitle(title=self.title)
        self.cp.addcampaigndescription(description=self.description)
        self.cp.addcampaignstartdate(year=2025, month=5, day=4)
        self.cp.addcampaignenddate(year=2025, month=6, day=4)
        self.cp.selectcampaignreward("CPA REWARD Configuration")
        self.cp.selectcampaignpartnerprogram("Referral Program")
        self.cp.selectpartnertype("Referral")
        self.cp.selectpartnertier("Registered Partner")
        self.cp.selectpartner("Absc pvt ltd")
        self.cp.addgoaltitle("Test Goal")
        self.cp.selectaction("Login")
        self.cp.adddestinationlink("test.com")
        self.cp.clicksavecampaign()
        message = self.cp.get_toast_message()
        assert message == "Campaign created successfully", "Error occurred while adding campaign"


    def test_addexistingcampaign(self, setup, login_fixture):
        self.driver = setup
        self.cp = CampaignObjects(self.driver)
        self.cp.clickcampaignmenu()
        self.cp.clickonaddcampaign()
        self.cp.addcampaigntitle("This test title")
        self.cp.addcampaigndescription("This test description")
        self.cp.addcampaignstartdate(year=2025, month=5, day=4)
        self.cp.addcampaignenddate(year=2025, month=6, day=4)
        self.cp.selectcampaignreward("CPA REWARD Configuration")
        self.cp.selectcampaignpartnerprogram("Referral Program")
        self.cp.selectpartnertype("Referral")
        self.cp.selectpartnertier("Registered Partner")
        self.cp.selectpartner("Absc pvt ltd")
        self.cp.addgoaltitle("Test Goal")
        self.cp.selectaction("Login")
        self.cp.adddestinationlink("test.com")
        self.cp.clicksavecampaign()
        message = self.cp.get_toast_message()
        print(message)
        assert message == "Campaign created successfully", "Error occurred while adding campaign"

