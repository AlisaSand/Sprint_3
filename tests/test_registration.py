import random
from selenium.webdriver.common.by import By
from random_username.generate import generate_username
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import ENTER_ACCOUNT_BUTTON, REGISTER_LINK, NAME_INPUT_ON_REGISTRATION_FORM, \
    EMAIL_INPUT_ON_REGISTRATION_FORM, PASSWORD_INPUT_ON_REGISTRATION_FORM, REGISTER_BUTTON, INCORRECT_PASSWORD_MESSAGE, \
    ENTERING_HEADER


def registration(driver, name, email, password):
    WebDriverWait(driver, 3) \
        .until(EC.element_to_be_clickable((By.XPATH, ENTER_ACCOUNT_BUTTON))) \
        .click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, REGISTER_LINK))) \
        .click()
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, NAME_INPUT_ON_REGISTRATION_FORM))) \
        .send_keys(name)
    driver.find_element(By.XPATH, EMAIL_INPUT_ON_REGISTRATION_FORM).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT_ON_REGISTRATION_FORM).send_keys(password)
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()


class TestRegistration:
    def test_error_appeared_when_incorrect_password_is_added_in_registration_form(self, driver):
        email = generate_username()[0] + str(random.randint(100, 999)) + '@gmail.com'
        name = email
        password = random.randint(0, 19999)
        print(email)
        registration(driver, name, email, password)
        actual_result = driver.find_element(By.XPATH, INCORRECT_PASSWORD_MESSAGE).text
        expected_result = 'Некорректный пароль'
        assert actual_result == expected_result, \
            'there should be an error when user entered password less than 6 symbols'

    def test_new_user_successfully_registered(self, driver):
        email = generate_username()[0] + str(random.randint(100, 999)) + '@gmail.com'
        name = email
        password = random.randint(100000, 10000000)
        print(email)
        registration(driver, name, email, password)
        actual_result = WebDriverWait(driver, 3) \
            .until(EC.visibility_of_element_located((By.XPATH, ENTERING_HEADER))) \
            .text
        expected_result = 'Вход'
        assert actual_result == expected_result, 'there should be a window for login after successfully registration'
