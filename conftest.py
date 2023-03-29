import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from random_username.generate import generate_username
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import ENTER_ACCOUNT_BUTTON, REGISTER_LINK, NAME_INPUT_ON_REGISTRATION_FORM, \
    EMAIL_INPUT_ON_REGISTRATION_FORM, PASSWORD_INPUT_ON_REGISTRATION_FORM, REGISTER_BUTTON, \
    EMAIL_INPUT_ON_ENTERING_FORM, PASSWORD_INPUT_ON_ENTERING_FORM, ENTER_BUTTON, ENTERING_HEADER

url = 'https://stellarburgers.nomoreparties.site/'


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1200,600')

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def login_as_new_user(driver):
    email = generate_username()[0] + str(random.randint(100, 999)) + '@gmail.com'
    name = email
    password = random.randint(100000, 10000000)
    print(email)

    WebDriverWait(driver, 3) \
        .until(EC.visibility_of_element_located((By.XPATH, ENTER_ACCOUNT_BUTTON))) \
        .click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, REGISTER_LINK))) \
        .click()

    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, NAME_INPUT_ON_REGISTRATION_FORM)))\
        .send_keys(name)
    driver.find_element(By.XPATH, EMAIL_INPUT_ON_REGISTRATION_FORM).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT_ON_REGISTRATION_FORM).send_keys(password)
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()

    WebDriverWait(driver, 12).until(
        EC.visibility_of_element_located((By.XPATH, ENTERING_HEADER)))
    driver.find_element(By.XPATH, EMAIL_INPUT_ON_ENTERING_FORM).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT_ON_ENTERING_FORM).send_keys(password)
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
