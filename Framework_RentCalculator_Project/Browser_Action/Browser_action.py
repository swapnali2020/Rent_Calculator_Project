from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import os
from Framework_RentCalculator_Project.test_data.test_data_file import *
from datetime import datetime

class Browser_Action():

    def __init__(self,browser,wait_time):
        self.browser = browser
        self.spdriver = None
        self.get_spdriver()
        self.wait = WebDriverWait(self.spdriver,wait_time)

    def get_spdriver(self):
        if self.browser == 'chrome':
            self.spdriver = webdriver.Chrome(executable_path= chrome_driver_path)
            self.spdriver.maximize_window()
            self.spdriver.implicitly_wait(10)

        elif self.browser == 'firefox':
            self.spdriver = webdriver.Firefox(executable_path= firefox_driver_path)
            self.spdriver.maximize_window()
            self.spdriver.implicitly_wait(10)

        elif self.browser == 'edge':
            self.spdriver = webdriver.Edge(executable_path=  edge_driver_path)
            self.spdriver.maximize_window()
            self.spdriver.implicitly_wait(10)

    def click_element(self,selector):
        element = self.wait.until(EC.presence_of_element_located((selector[0], selector[1])))
        element.click()

    def input_text(self,selector,value):
        element = self.wait.until(EC.presence_of_element_located((selector[0], selector[1])))
        element.clear()
        element.send_keys(value)

    def get_all_elements(self,selector):
        elements = self.wait.until(EC.presence_of_all_elements_located((selector[0], selector[1])))
        return elements

    def get_element_text(self,selector):
        element = self.wait.until(EC.presence_of_element_located((selector[0], selector[1])))
        return element.text

    def verify_element_is_visible(self,selector):
        self.wait.until(EC.visibility_of_element_located((selector[0], selector[1])))

    def select_value_from_dropdown(self, selector, value):
        element = self.wait.until(EC.presence_of_element_located((selector[0], selector[1])))
        select_obj = Select(element)
        select_obj.select_by_visible_text(value)


    def take_screen_shot(self,prefix):
        cur_time = str(datetime.time(datetime.now()))
        current_time = cur_time.replace(":","_").replace(".", "_")
        file_name = f"{prefix}_{current_time}.png"
        if os.path.isdir(IMAGE_DIR):
            self.spdriver.save_screen_shot(IMAGE_DIR, file_name)
        elif os.mkdir(IMAGE_DIR):
            self.spdriver.save_screen_shot(IMAGE_DIR,file_name)



