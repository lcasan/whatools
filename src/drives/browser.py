from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time 
from PIL import Image

class Browser():
    def __init__(self):
        self.drive = webdriver.Firefox(executable_path="src/drives/firefox/geckodriver")
        self.drive.maximize_window()
        self.drive.get("https://web.whatsapp.com")
        
        #QR authentication:
        time.sleep(5)
        qr = True
        while qr:
            print('waiting...')
            qr = self.code_qr()
            time.sleep(2)

        
    def code_qr(self):
        try:
            self.drive.find_element(By.TAG_NAME, 'canvas')
        except:
            return False
        return True

    def send_message(self, msg, groups, img, text, path):
        for group in groups:
            search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
            search_box = WebDriverWait(self.drive, 500).until(
                EC.presence_of_element_located((By.XPATH, search_xpath))
            )

            search_box.clear()
            pyperclip.copy(group)
            search_box.send_keys(Keys.CONTROL + 'V')
            time.sleep(2)

            #find group:
            group_xpath = f'//span[@title="{group}"]'
            group_title = self.drive.find_element(By.XPATH, group_xpath)
            group_title.click()
            time.sleep(2)
            

            if img:
                #select clip button:
                clip_xpath = f'//span[@data-icon="clip"]'
                clip = self.drive.find_element(By.XPATH, clip_xpath)
                clip.click()
                time.sleep(1)

                #add file path
                self.drive.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(path)
                time.sleep(2)
                input_box = self.drive.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')

                if text:    
                    #Send msg
                    pyperclip.copy(msg)
                    input_box.send_keys(Keys.CONTROL + "V")
                    time.sleep(2) 

                input_box.send_keys(Keys.ENTER)
            else:
                input_box = self.drive.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                pyperclip.copy(msg)
                input_box.send_keys(Keys.CONTROL + "V")
                time.sleep(3) 
                input_box.send_keys(Keys.ENTER)
                
            
            

            
            



