# pip3 install -U selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# similar to setting property and pass path of chromedriver file
driver = webdriver.Chrome(executable_path='/Users/soumyamishra/PycharmProjects/PythonSelenium21/chromedriver')

# implicit wait
driver.implicitly_wait(5)

# launching URL
driver.get("https://www.google.com")

# finding element and perform send keys
search_element = driver.find_element(By.NAME, 'q')
print(type(search_element))
search_element.send_keys("Warner Brothers")

# get list of elements from the suggestion
options_list = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
print(type(options_list))
print(len(options_list))

# click on some matching criteria
for element in options_list:
    print(element.text)
    if element.text == 'warner brothers net worth':
        element.click()
        break

print(driver.title)
if driver.title.__contains__('warner brothers net worth'):
    print('Title matched as expected')

# Thread.sleep
time.sleep(5)

# quitting the browser
driver.quit()
