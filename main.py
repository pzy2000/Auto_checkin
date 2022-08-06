import time

from selenium import webdriver
from selenium.webdriver.common.by import By

path = 'msedgedriver.exe'
driver = webdriver.Edge(path)
driver.get('https://www.yuruyun.com/auth/login')
user = driver.find_element(By.ID, 'email')
username = "2592532554@qq.com"
password = driver.find_element(By.ID, "password")
passwd = "112233abcD"

user.send_keys(username)
password.send_keys(passwd)

log_btn = driver.find_element(By.ID, "login_submit")
log_btn.click()
time.sleep(6)

mainWindow = driver.current_window_handle
driver.switch_to.window(mainWindow)

'''close_shit = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[3]/button')
close_shit.click()'''  # 免费用户需要启用
try:
    sign_btn = driver.find_element(By.ID, 'checkin')
    sign_btn.click()
    print('签到完成！')

except:
    print('已经签到过了！')

time.sleep(6)
driver.quit()
