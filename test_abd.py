import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import  time


def setup_function():
    global driver
    browser = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=browser)
    driver.get('https://stage.alnafi.com/auth/signin')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('anus@gmail.com', 'anus@123'),
        ('ali@gmail.com', 'ali@123')
    ]
@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.ID,'Username/ Email').send_keys(username)
    time.sleep(3)
    driver.find_element(By.ID, 'Password').send_keys(password)
    time.sleep(3)


