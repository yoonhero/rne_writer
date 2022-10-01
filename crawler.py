from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Crawler():
    def __init__(self):
        self.browser = webdriver.Chrome("./chromedriver.exe")
        self.num = 79

        self.login()

    def login(self): 
        self.browser.get('https://welcomerne.com/login.jsp')

        self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[1]/td/div/input").send_keys("ysh")

        self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[2]/td/div/input").send_keys("6223")


        self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[3]/td/input").click()

    def write(self, author, contents):
        try:
            self.num += 1

            self.browser.get("https://welcomerne.com/write.jsp?bbsType=1&searchWord=null")

            self.browser.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[1]/td/input").send_keys(f"오늘의 명언 {self.num}")
            self.browser.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[2]/td/textarea").send_keys(f"{contents}\n-{author}-\n\nGenerated With GPT2")

            verification_code = self.browser.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[3]/td[1]").text
            self.browser.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[3]/td[2]/input[1]").send_keys(verification_code)

            time.sleep(4)

            self.browser.find_element(By.XPATH,"/html/body/div/div/form/input").click()

            
        except:
            alert = self.driver.switch_to_alert()
            alert.accept()
            time.sleep(60)

    def quit(self):
        self.browser.quit()