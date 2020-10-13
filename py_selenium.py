import os
from selenium import webdriver

#chromedriver = r"\Users\spbac\Downloads\chromedriver_win32\chromedriver.exe"
#os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(executable_path= 'C:/Users/spbac/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("http://stackoverflow.com")
driver.quit()