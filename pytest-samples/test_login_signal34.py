import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# test cases to test the Signal34 Login

@pytest.fixture(params=["chrome", "firefox", "MicrosoftEdge"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    if request.param == "MicrosoftEdge":
        web_driver = webdriver.Edge()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class TestLoginSuccesful(BasicTest):
    def setup_method(self, method):
        self.vars = {}

    def test_login_succesful(self):
        url = "https://signal34.com/"

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(
            By.CSS_SELECTOR, ".signal34-bnt-sign-in").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(
            "jvictorhugo@hotmail.com")
        self.driver.find_element(By.ID, "password").send_keys("qwert12345")
        self.driver.find_element(
            By.CSS_SELECTOR, ".signal34-bnt-primary").click()

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.ID, "actions-menu-toggle")))

        with pytest.raises(Exception) as NoSuchElementException:
            self.driver.find_element(By.CSS_SELECTOR, ".signal34-bnt-sign-in")
            
    
class TestLoginInvalidUser(BasicTest):
    def setup_method(self, method):
        self.vars = {}
    def test_login_failed(self):
        url = "https://signal34.com/"        

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(
            By.CSS_SELECTOR, ".signal34-bnt-sign-in").click()
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys(
            "fake_user@email.com")
        self.driver.find_element(By.ID, "password").send_keys("12345")
        self.driver.find_element(
            By.CSS_SELECTOR, ".signal34-bnt-primary").click()

        with pytest.raises(Exception) as TimeoutException:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located(
              (By.ID, "actions-menu-toggle")))

class TestLoginEmpty(BasicTest):
    def setup_method(self, method):
        self.vars = {}
    def test_login_failed(self):
        url = "https://signal34.com/"        

        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(
            By.CSS_SELECTOR, ".signal34-bnt-sign-in").click()
        self.driver.find_element(
            By.CSS_SELECTOR, ".signal34-bnt-primary").click()

        with pytest.raises(Exception) as TimeoutException:
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located(
              (By.ID, "actions-menu-toggle")))