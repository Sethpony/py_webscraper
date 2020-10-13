from selenium import webdriver

# browser = webdriver.Chrome(executable_path = "C:\Users\spbac\Downloads\chromedriver_win32\chromedriver.exe")
browser = webdriver.Chrome()
browser.get('www.yahoo.com')
assert browser.title == 'Yahoo'