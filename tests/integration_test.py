import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


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

    def test_login(self):

        self.driver.get("https://pillio.pythonanywhere.com/login")
        # get the search textbox

        self.search_login= self.driver.find_element_by_name("email")
        # enter search keyword and submit
        self.search_login.send_keys("abin@gmail.com")

        self.search_pass = self.driver.find_element_by_name("password")
        # enter search keyword and submit
        self.search_pass.send_keys("123456")

        self.driver.find_element_by_css_selector('.button').click()

        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        #self.driver.findElement(By.tagName("h1")).isDisplayed()
        titleOfWebPage = self.driver.title
        # verify title is bing
        self.assertTrue((titleOfWebPage != "Pill.IO"),
                        "webpage title is not matching")

    def test_sign_up(self):

        ### when you run you have to change the info becasue this acct is already created
        self.driver.get("https://pillio.pythonanywhere.com/signup")


        self.search_login = self.driver.find_element_by_name("email")

        self.search_login.send_keys("abe@gmail.com")

        self.search_pass = self.driver.find_element_by_name("password")
        self.search_pass.send_keys("123456")

        self.search_pass = self.driver.find_element_by_name("first_name")
        self.search_pass.send_keys("abe")

        self.search_pass = self.driver.find_element_by_name("last_name")
        self.search_pass.send_keys("levandowski")

        self.search_pass = self.driver.find_element_by_name("dob")
        self.search_pass.send_keys("09/03/1995")

        s = self.driver.find_element_by_xpath("//input[@type='file']")

        #pic = self.driver.find_element_by_name("image")
        s.send_keys("/Users/AbinCheriyan/Documents/GitHub/project-pill-io/tests/cal.png")

        self.driver.find_element_by_css_selector('.button').click()


        titleOfWebPage = self.driver.title
        self.assertTrue((titleOfWebPage != "Pill.IO"),
                            "webpage title is not matching")

    def test_sign_up_fail(self):
        ### when you run you have to change the info becasue this acct is already created
        self.driver.get("https://pillio.pythonanywhere.com/signup")

        self.search_login = self.driver.find_element_by_name("email")

        self.search_login.send_keys("abe@gmail.com")

        self.search_pass = self.driver.find_element_by_name("password")
        self.search_pass.send_keys("123456")

        self.search_pass = self.driver.find_element_by_name("first_name")
        self.search_pass.send_keys("abe")

        self.search_pass = self.driver.find_element_by_name("last_name")
        self.search_pass.send_keys("levandowski")

        self.search_pass = self.driver.find_element_by_name("dob")
        self.search_pass.send_keys("09/03/1995")

        s = self.driver.find_element_by_xpath("//input[@type='file']")

        # pic = self.driver.find_element_by_name("image")
        s.send_keys("/Users/AbinCheriyan/Documents/GitHub/project-pill-io/tests/cal.png")

        self.driver.find_element_by_css_selector('.button').click()

        titleOfWebPage = self.driver.find_elements_by_class_name("c")
        print(titleOfWebPage)
        self.assertTrue((titleOfWebPage != " Email address already exists"),
                        "signup is not matching")
    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()