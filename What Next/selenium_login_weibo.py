from selenium import webdriver
from time import sleep

class Driver:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.url = 'https://weibo.com/'
        self.account = 'leogwork@gmail.com'
        self.pwd = 'ksxyhzgdnz007'
    def open(self):
        self.driver.get(self.url)
        sleep(10)
        self.driver.find_element_by_id('loginname')
        sleep(1)
        self.driver.find_element_by_id('loginname').send_keys(self.account)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[2]/div/input")
        sleep(1)
        self.driver.find_element_by_css_selector(".password > div:nth-child(1) > input:nth-child(1)").send_keys(self.pwd)
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[3]/div[6]/a").click()
    def close(self):
        self.driver.close()
driver = Driver()
driver.open()