import tarfile
import time
from matplotlib.pyplot import text
from selenium import webdriver



translate_result_list = []

class translate_on_ChromeWeb():
    def __init__(self):
        self.browser_driver = webdriver.Chrome()
        self.browser_driver.get('https://translate.google.co.jp/?hl=ja')
        time.sleep(20)
    
    def search_on_chrome(self, file_line):
        search_box = self.browser_driver.find_element_by_class_name("er8xn")
        search_box.send_keys(file_line)
        time.sleep(10)
        temporary_list = []
        
        search_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[{}]'.format(1)
        result_text = search_box.find_element_by_xpath(search_xpath)
        time.sleep(3)
        temporary_list.append(result_text.text)
        print(temporary_list)
        
        
        temp_text = ''.join(temporary_list)
        translate_result_list.append(temp_text)
        search_box.clear()

    def close_chrome_file(self):
        time.sleep(5)
        self.browser_driver.quit()

# a = translate_on_chrome()
# a.search_on_chrome('hello world')
# a.search_on_chrome('hello japan')
# a.close_chrome_file()

# print(translate_result_list)