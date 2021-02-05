import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddCart(unittest.TestCase):
    def setUp(self):
        PATH = 'C:\Program Files (x86)\chromedriver.exe'
        options = Options()
        options.add_argument('user-data-dir=C:\\Users\\46um\\AppData\\Local\\Google\\Chrome\\User Data')

        self.driver = webdriver.Chrome(PATH, options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://bhinneka.com')
    
    def test_add_item_cart(self):
        self.search_field = self.driver.find_element_by_xpath("//div[@class='css-18z11p']/input")
        self.search_field.send_keys('mouse')

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "css-yhj6ev"))
            )

        except:
            self.driver.quit()
        
        prods_title = self.driver.find_elements_by_class_name("css-1yq2xbk")
        for title in prods_title:
            if 'mouse' not in title.text.lower():
                print('wrong result')
        
        prods_title[1].click()
        item_name = self.driver.find_element_by_tag_name("h2").text
        btn_tambah = self.driver.find_element_by_class_name('css-1t6w53m')
        btn_tambah.click()

        val_cart = self.driver.find_element_by_class_name('css-jns98h').text
        if val_cart != '1':
            print('wrong val on cart')
        
        btn_keranjang = self.driver.find_element_by_xpath("//div[@class='css-1yt4s5m']/div/button[@class='css-9vi8jg']")
        btn_keranjang.click()
        
        item_incart = self.driver.find_element_by_xpath("//div[@class='css-16ff5hw etma6yr3']/h4").text
        val_sub = self.driver.find_element_by_xpath("//div[@class='css-dza15n e1lsoz2m2']/p/span").text

        if '1' not in val_sub:
            print('wrong value on subtotal')
        elif item_incart != item_name:
            print('wrong item')
        else:
            pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()