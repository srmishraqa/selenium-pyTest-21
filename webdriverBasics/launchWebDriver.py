# pip3 install -U selenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/Users/soumyamishra/PycharmProjects/PythonSelenium21/chromedriver')
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
