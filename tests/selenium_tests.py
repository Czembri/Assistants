import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Testmain(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_main_to_create(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        createbtn = driver.find_element_by_name("createbtn")        
        createbtn.click()

    def test_create_to_main(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/create")
        createbtn = driver.find_element_by_tag_name("h1")        
        createbtn.click()

    def create_user(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/create")
        createbtn = driver.find_element_by_name("fname")
        createbtn.send_keys("Jola")
        createbtn = driver.find_element_by_name("lname")
        createbtn.send_keys("Makłowicz")
        createbtn = driver.find_element_by_name("email")
        createbtn.send_keys("jola.maklowicz@gmail.com")
        driver.find_element_by_xpath("//select[@name='occupation']/option[text()='2nd Pressman']").click()
        submit = driver.find_element_by_name("submit")
        submit.click()


    def tearDown(self):
        self.driver.close()

    

if __name__ == "__main__":
    unittest.main()
