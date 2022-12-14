from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Crawler():
    def __init__(self):
        self.browser = webdriver.Chrome("./chromedriver.exe")

        self.login()
        
        self.browser.get("https://welcomerne.com/bbs.jsp?bbsType=1")

        i = 0
        while True:
            i += 1
            text = self.browser.find_element(By.XPATH, f"/html/body/div[4]/div/table/tbody/tr[{i}]/td[2]/a").text
            if text[0:6] == "오늘의 명언":
                self.num = int(text[-3:])
                break

    def login(self): 
        self.browser.get('https://welcomerne.com/login.jsp')

        self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[1]/td/div/input").send_keys("ysh")

        self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[2]/td/div/input").send_keys("6223")


        self.browser.find_element(By.XPATH,"/html/body/form/table/tbody/tr[3]/td/input").click()

    def write(self, author, contents):
        self.num += 1

        
        try:
            self.browser.get("https://welcomerne.com/write.jsp?bbsType=1&searchWord=null")
            self.browser.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[1]/td/input").send_keys(f"오늘의 명언 {self.num}")
            self.browser.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[2]/td/textarea").send_keys(f"{contents}\n-{author}-\n\nGenerated With GPT2")

            verification_code = self.browser.find_element(By.XPATH, "/html/body/div/div/form/table/tbody/tr[3]/td[1]").text
            self.browser.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[3]/td[2]/input[1]").send_keys(verification_code)

            time.sleep(3)

            self.browser.find_element(By.XPATH,"/html/body/div/div/form/input").click()

        except:
            print("Error Occured")
            alert = self.browser.switch_to.alert
            alert.accept()

            time.sleep(120)

    def delete(self):
        try:
            self.browser.get("https://welcomerne.com/post.jsp?pageNumber=1&bbsType=998&searchWord=null")

            self.browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a").click()

            self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/a[2]").click()

            time.sleep(0.1)

            alert = self.browser.switch_to.alert
            alert.accept()

            time.sleep(1)
        except:
            time.sleep(14)

    def quit(self):
        self.browser.quit()





if __name__ == "__main__":
    crawl = Crawler()

    while True:
        crawl.delete()