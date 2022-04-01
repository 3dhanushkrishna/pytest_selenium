from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture()
def setUp():
    global driver,product
    product = input("enter the product to be search: ")
    print("testcase started")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_searchproduct(setUp):
    driver.get("https://www.flipkart.com/")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(1)
    driver.find_element_by_name("q").send_keys(product)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 1000)")
    time.sleep(5)
    s = driver.find_element_by_name("q")
    action = ActionChains(driver)
    action.context_click(s)
    action.perform()
    time.sleep(5)
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    action.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(3)



