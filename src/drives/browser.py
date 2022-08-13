from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time 

class Browser():
    def __init__(self):
        self.drive = webdriver.Firefox(executable_path="src/drives/firefox/geckodriver-v0.31.0-win64/geckodriver.exe")
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
    
    def find_group(self, group):
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

    def send_message(self, msg, groups, img, text, path):
        for group in groups:
            self.find_group(group)

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
                    time.sleep(2)
                    input_box.send_keys(Keys.CONTROL + "V")
                    time.sleep(4) 

                input_box.send_keys(Keys.ENTER)
            else:
                input_box = self.drive.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                pyperclip.copy(msg)
                input_box.send_keys(Keys.CONTROL + "V")
                time.sleep(3) 
                input_box.send_keys(Keys.ENTER)
                
    def clean_chat(self, groups):
        for group in groups:
            self.find_group(group)

            #select menu
            menu_xpath = f'/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div/div/span'
            clip = self.drive.find_element(By.XPATH, menu_xpath)
            clip.click()
            time.sleep(1)

            #select option
            self.drive.find_element(By.XPATH, f'//li[@data-testid="mi-clear"]').click()
            time.sleep(1)

            self.drive.find_element(By.XPATH, f'//div[@data-testid="popup-controls-ok"]').click()
            time.sleep(1)
            
            try:
                self.drive.find_element(By.XPATH, f'//div[@data-testid="popup-controls-ok"]').click()
            except:
                time.sleep(1)
                



            

    


