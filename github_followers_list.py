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
    
    def repoSearch(self,keyword,page):#adds the repo on the page to the list as many as the number of pages entered
        #find search bar
        searchInput=self.browser.find_element(By.NAME,"q")
        
        #type the keyword in the search bar
        searchInput.send_keys(keyword)
        
        #press enter
        searchInput.send_keys(Keys.ENTER)
        time.sleep(3)
        self.repo_link=[]
        i=1       
        while i<page:
            self.browser.get("https://github.com/search?p="+str(i)+"&q=python&type=Repositories")
            i+=1
            time.sleep(2)#load wait 
            repos=self.browser.find_elements(By.XPATH,"/html/body/div[1]/div[5]/main/div/div[3]/div/ul/li")
            for repo in repos :
                self.repo_link.append(repo.find_element(By.TAG_NAME,'a').get_attribute("href"))

    
        
        
        
        
#create object
github=GitHub(username,password)
github.signIn()
github.repoSearch("python",5)
print(github.repo_link)
        
        
        
        
