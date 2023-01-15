from githubUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class GitHub:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password
        
        self.followers=[]
    
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(3)
        
        usernameInput=self.browser.find_element(By.NAME,"login")
        passowrdInput=self.browser.find_element(By.NAME,"password")
        
        #user info input
        usernameInput.send_keys(self.username)
        passowrdInput.send_keys(self.password)
        
        #login
        button=self.browser.find_element(By.NAME,"commit")
        button.click()
        time.sleep(3)
    
    def repoSearch(self,keyword):#just one page ??
        #find search bar
        searchInput=self.browser.find_element(By.NAME,"q")
        
        #type the keyword in the search bar
        searchInput.send_keys(keyword)
        
        #press enter
        searchInput.send_keys(Keys.ENTER)
        time.sleep(3)
        
        repos=self.browser.find_elements(By.XPATH,"/html/body/div[1]/div[5]/main/div/div[3]/div/ul/li")
        for repo in repos :
            print(repo.find_element(By.TAG_NAME,'a').text)
            print(repo.find_element(By.TAG_NAME,'a').get_attribute("href"))
            print("---------------")
        
        
        
#create object
github=GitHub(username,password)
github.signIn()
github.repoSearch("python")
        
        
        
        
