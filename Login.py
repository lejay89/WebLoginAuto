# depends on:
# 1. chromedriver

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By # 内置定位器策略集
from selenium.webdriver.support import expected_conditions as EC # 内置预期条件函数

url = 'https://www.baidu.com/'

driver = webdriver.Chrome('D:/tools/chromedriver')
driver.get(url)

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('洗烘套装')
driver.find_element_by_xpath('//*[@id="su"]').click()

try:
    WebDriverWait(driver,60).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="1"]/div/div/div[2]/div[1]/div[1]/div/a')))
except:
    driver.close()

# 点击右边热搜第一条
driver.find_element_by_xpath('//*[@id="1"]/div/div/div[2]/div[1]/div[1]/div/a').click()


# 获取当前所有页面窗口的句柄
windows = driver.window_handles
# 切换至最新打开的窗口 为啥-1？
driver.switch_to.window(windows[-1])
#print (driver.current_url)


#输出百度搜索的结果条数
result = driver.find_element_by_xpath('//*[@id="tsn_inner"]/div[2]/span')
print(result.text)


