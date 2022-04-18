import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SearchText(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        inst.driver = webdriver.Chrome()
        PATH = "/usr/local/bin/chromedriver"
        inst.driver.implicitly_wait(5)
        inst.driver.maximize_window()

        inst.driver.get("https://pillio.pythonanywhere.com/")

    def test_site_redirect(self):


        #self.search_field = self.driver.find_element_by_class_name("title")


        lists = self.driver.find_element_by_class_name("title")
        self.assertIn("Welcome to Pill.io!", self.driver.title)
        #self.assertEqual(11, len(lists))

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.send_keys("Python class")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, len(list_new))

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()