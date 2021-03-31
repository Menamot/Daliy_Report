# -*- coding =utf-8 -*-
# @Time : 2021/3/27 19:54
# @Author : 陈文龙
# @File : Self_Report.py
# @Software : PyCharm

# 每次版本更新时，需要更新节点数据
# 更新方式为，用一个没有填过每日一报的账户登录，然后在开发者工具中找到对应的节点，copy对应的xpath路径

import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# list用于存放用户账号和密码
list=[['18124723', '200714cheN'], ['18124719', 'Ep921305'], ['18124722', 'SIMONzlx959'], ['18124610', 'LWh010202']]

for i in list:
    username = i[0]
    passwd = i[1]

    options = webdriver.ChromeOptions()
    options.add_argument('user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"')  # 添加UA
    options.add_argument('--headless')  # 无界面模式
    options.add_argument('window-size=1200x600')  # 调整虚拟窗口大小
    options.add_argument('--no-sandbox')  # 禁用沙盒模式
    options.add_argument('--disable-gpu')  # 禁用GPU加速

    browser = webdriver.Chrome(chrome_options=options)  # 创建浏览器对象
    browser.get('https://selfreport.shu.edu.cn/DayReport.aspx')
    input_username = browser.find_element_by_id('username')  # 寻找id为username的节点
    input_username.send_keys(username)  # 向username节点传入账号
    input_passwd = browser.find_element_by_id('password')
    input_passwd.send_keys(passwd)
    login = browser.find_element_by_id('submit')
    login.click()  # 点击登录

    # 下面开始会随着版本更新而失效
    chengnuo = browser.find_element_by_xpath('//*[@id="p1_ChengNuo-inputEl-icon"]')
    chengnuo.click()  # 点击承诺
    dansSH = browser.find_element_by_xpath('//*[@id="fineui_7-inputEl-icon"]')
    dansSH.click()  # 点击在上海
    wait = WebDriverWait(browser,10)
    zhuxiao = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fineui_9-inputEl-icon"]')))
    zhuxiao.click()  # 点击住校
    wait = WebDriverWait(browser, 10)
    jiating = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fineui_12-inputEl-icon"]')))
    jiating.click()  # 点击家庭


    # 下面代码很有可能因为版本更新而失效
    tijiao = browser.find_element_by_xpath('/html/body/form/div[5]/div/div[2]/div[2]/div/div/a[1]')
    tijiao.click()  # 点击提交
    wait = WebDriverWait(browser, 3)
    queren = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fineui_36"]')))
    queren.click()  # 点击确认提交
    print("等待提交10秒，用户为%s" % username)
    time.sleep(10)
    result = re.findall('<div class="f-messagebox-message">(.*?)</div>', browser.page_source)
    print(result)
    print("若出现提交成功则成功，否则失败")
    browser.close()

