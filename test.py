import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://translate.google.co.jp/?hl=ja')
time.sleep(5)
search_box = driver.find_element_by_class_name("er8xn")
search_box.send_keys('By the way, UDS trigger also can self-learn both of two side at one time, self-learn P and then self-learn NP immediately. And UAES mainly uses this method daily.')
time.sleep(10)

result_text = search_box.find_elements_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]')
print(result_text[0].text)
time.sleep(5)
driver.quit()
//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span[1]/span
//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div[6]/div/div[1]/span[1]/span[2]/span