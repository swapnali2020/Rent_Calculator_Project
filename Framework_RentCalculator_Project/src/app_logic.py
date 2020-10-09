from Framework_RentCalculator_Project.Browser_Action.Browser_action import *
from Framework_RentCalculator_Project.src.locators import *
from Framework_RentCalculator_Project.test_data.test_data_file import *

class AppFunction(Browser_Action):
    def __init__(self,browser,url,wait_time):
        self.url = url
        super().__init__(browser,wait_time)
        self.launch_app()
    def launch_app(self):
        self.spdriver.get(self.url)




#Get Mortgage Details
    def get_mortgage_link(self):
        self.click_element(MORTGAGE_LINK)
    def get_calculate(self):
        self.click_element(CALCULATE)

    def get_monthly_pay(self):
        (self.get_element_text(MORTGAGE_MONTHLY_PAY))



