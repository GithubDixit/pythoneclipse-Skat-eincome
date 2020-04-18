from selenium import webdriver


import time

# open Firefox Browser
#from methods import methods

driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
driver.get("http://10.9.182.12/")

time.sleep(3)

# Move to popup window to add username and password
print(driver.current_window_handle)  # 18 <-- Parent
handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
driver.maximize_window()