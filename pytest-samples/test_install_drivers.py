import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Using web drivers
@pytest.mark.skip(reason="Do not run in CI")
def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.quit()
    
def test_edge_session():
    service = EdgeService(
        executable_path=EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.quit()

def test_firefox_session():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.quit()
