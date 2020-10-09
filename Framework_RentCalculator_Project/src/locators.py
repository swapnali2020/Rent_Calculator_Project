from selenium.webdriver.common.by import By
from Framework_RentCalculator_Project.test_data.test_data_file import *

XPATH = By.XPATH
ID = By.ID
LINK_TEXT =By.LINK_TEXT
NAME = By.NAME
CSS_SELECTOR = By.CSS_SELECTOR


MORTGAGE_LINK= (XPATH, "//body/div[@id='contentout']/div[@id='right']/div[@id='othercalc']/div[@id='occontent']/a[1]")
CALCULATE = (XPATH, "//input[@value= 'Calculate']")
MORTGAGE_MONTHLY_PAY=(XPATH,"//h2[@class = 'h2result']")
