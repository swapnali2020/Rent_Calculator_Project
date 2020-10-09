import os
url = "https://www.calculator.net/rent-calculator.html"
browser = 'chrome'
wait_time = 20

chrome_driver_path = "/Users/palashjborah/Swapnali/pythonProject/Selenium/Driver/Chrome/chromedriver"
firefox_driver_path = "/Users/palashjborah/Swapnali/pythonProject/Selenium/Driver/Firefox/geckodriver"
edge_driver_path = "/Users/palashjborah/Swapnali/Learning//Driver/Edge/edgedriver"

CUR_DIR = os.getcwd()
LOG_DIR= os.path.join(CUR_DIR,"log")
IMAGE_DIR = os.path.join(CUR_DIR,"image")
test_data_path = os.path.join(CUR_DIR,"test_data")
excel_file_path = os.path.join(test_data_path,"testexcel.xsls")


