from ast import keyword
import requests
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import wget

def downloadall():
    with open("downloadlinks.txt","r") as f:
        links = f.read().splitlines()
        for i in range(len(links)):
            wget.download(links[i], out =str(i+1)+".mp4")


def downloader(number,url):
    listt = []
    url = url
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')  
    chrome_options.add_argument('--headless')  
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver.get(url)
    time.sleep(30)
    quality = 144
    driver.find_element(By.XPATH,'//*[@id="primary"]/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/div/button').click()
    try:
        if  driver.find_element(By.XPATH, '//*[@id="144p"]/div/span/span').is_displayed():
            print(f"144P exists")
            quality = 144
    except:
        pass
    try:
        
        if  driver.find_element(By.XPATH, '//*[@id="240p"]/div/span/span').is_displayed():
            print(f"240P exists")
            quality = 240
    except:
        pass
    try:
        if  driver.find_element(By.XPATH, '//*[@id="360p"]/div/span/span').is_displayed():
            print(f"360P exists")
            quality = 360
    except:
        pass
    try:
        if  driver.find_element(By.XPATH, '//*[@id="720p"]/div/span/span').is_displayed():
            print(f"720P exists")
            quality = 720
    except:
        pass
    try:    
        if  driver.find_element(By.XPATH, '//*[@id="1080p"]/div/span/span').is_displayed():
            print(f"1080P exists")
            quality = 1080
    except:
        pass
    driver.find_element(By.XPATH, f'//*[@id="{quality}p"]/div/span/span').click()
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(5)
    url = driver.current_url
    print(url)
    driver.close()
    return url
                                  
def getlinks(url):
    with open("links.txt","w+") as f:
        f.write("")
        f.close()
    url = url 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')    
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
    driver.get(url)
    time.sleep(10)
    list = driver.find_elements(By.CLASS_NAME,  "thumb-content")
    for i in list:
        link = i.find_element(By.TAG_NAME,"a")
        ll = link.get_attribute("href")
        with open("links.txt","a+") as f:
            f.write(ll)
            f.write("\n")
    driver.close()
    with open("links.txt","r") as f:
        links = f.read().splitlines()
        print(str(len(links)) + " Videos were found!")
        for b in range(len(links)):
            print("Video #" + str(b))
            #wget.download(downloader(b,links[b]), out =str(b)+".mp4")
            with open("downloadlinks.txt","a+") as f:
                f.write(downloader(b,links[b]))
                f.write("\n")
with open("downloadlinks.txt","w") as f:
    f.write("")
    f.close()
getlinks(input("link?"))
downloadall()
