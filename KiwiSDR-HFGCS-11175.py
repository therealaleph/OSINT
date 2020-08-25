import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class initiate:
    def __init__(self):
        self.driver = webdriver.Firefox()
        # YOU MAY USE ANY KIWISDR WEBSITE, JUST REPLACE WITH THE LINK BELOW 
        self.driver.get("http://ciw321.cfars.ca:8174/?dqy73e8")
        # ^
        time.sleep(5) #CHANGE THE SLEEP TIME ACCORDINGLY, IT DEPENDS ON YOUR OWN AND THE KIWISDR SPEED
        self.driver.find_element_by_id("id-freq-input").send_keys("11175") #CHANGE 11175 to 8992,4274 or 15016 
        self.driver.find_element_by_id("id-freq-input").send_keys(Keys.RETURN)
        self.driver.find_element_by_id("id-readme-hide").click()
        self.driver.find_element_by_id("4-id-mode-col").click()
        self.driver.find_element_by_id("id-nav-optbar-agc").click()
        slope = self.driver.find_element_by_id("input-slope")
        slider = self.driver.find_element_by_id("input-threshold")
        decay = self.driver.find_element_by_id("input-decay")
        for i in range(60):
            slider.send_keys(Keys.RIGHT)
        for i in range(1):
            slope.send_keys(Keys.LEFT)
        for i in range(750):
            decay.send_keys(Keys.LEFT)
        


initiate()
