import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import  time


def setup_function():
    global driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://stage.alnafi.com/auth/signin')
    driver.maximize_window()

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('abdeali@gmail.com', 'abdeali@123'),
        ('abd@gmail.com', 'abd@123')
    ]
@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My pytest login")
    driver.find_element(By.ID,'Username/ Email').send_keys(username)
    time.sleep(3)
    driver.find_element(By.ID, 'Password').send_keys(password)
    time.sleep(3)


