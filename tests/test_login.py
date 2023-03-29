import random
from selenium.webdriver.common.by import By
from random_username.generate import generate_username
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PERSONAL_ACCOUNT, EMAIL_INPUT_ON_ENTERING_FORM, PASSWORD_INPUT_ON_ENTERING_FORM, \
    ENTER_BUTTON, CREATE_ORDER_BUTTON, ENTER_ACCOUNT_BUTTON, REGISTER_LINK, NAME_INPUT_ON_REGISTRATION_FORM, \
    EMAIL_INPUT_ON_REGISTRATION_FORM, PASSWORD_INPUT_ON_REGISTRATION_FORM, REGISTER_BUTTON, ENTERING_HEADER, \
    PASSWORD_RECOVERY_LINK, ENTERING_LINK_FROM_RECOVERY_PASSWORD_PAGE

REGISTERED_EMAIL = 'test1234@gmail.com'
REGISTERED_PASSWORD = 1234567


def login(driver, email, password):
    WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, EMAIL_INPUT_ON_ENTERING_FORM))) \
        .send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT_ON_ENTERING_FORM).send_keys(password)
    driver.find_element(By.XPATH, ENTER_BUTTON).click()
    actual_text = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, CREATE_ORDER_BUTTON))) \
        .text
    return actual_text


class TestLogin:
    def test_user_successfully_login_from_personal_account_page(self, driver):
        email = REGISTERED_EMAIL
        password = REGISTERED_PASSWORD

        WebDriverWait(driver, 3)\
            .until(expected_conditions.element_to_be_clickable((By.XPATH, PERSONAL_ACCOUNT)))\
            .click()
        actual_text = login(driver, email, password)
        expected_text = 'Оформить заказ'
        assert actual_text == expected_text, \
            'when user successfully registered buton "Войти" is changed on "Оформить заказ"'

    def test_user_successfully_login_from_main_page(self, driver):
        email = REGISTERED_EMAIL
        password = REGISTERED_PASSWORD
        print(email)

        WebDriverWait(driver, 3)\
            .until(EC.element_to_be_clickable((By.XPATH, ENTER_ACCOUNT_BUTTON)))\
            .click()
        actual_text = login(driver, email, password)
        expected_text = 'Оформить заказ'
        assert actual_text == expected_text, \
            'when user successfully registered buton "Войти" is changed on "Оформить заказ"'

    def test_user_successfully_login_from_recovery_password_page(self, driver):
        email = REGISTERED_EMAIL
        password = REGISTERED_PASSWORD
        print(email)

        WebDriverWait(driver, 3)\
            .until(expected_conditions.element_to_be_clickable((By.XPATH, ENTER_ACCOUNT_BUTTON)))\
            .click()
        WebDriverWait(driver, 3) \
            .until(expected_conditions.element_to_be_clickable((By.XPATH, PASSWORD_RECOVERY_LINK))) \
            .click()
        driver.find_element(By.XPATH, ENTERING_LINK_FROM_RECOVERY_PASSWORD_PAGE).click()
        actual_text = login(driver, email, password)
        expected_text = 'Оформить заказ'
        assert actual_text == expected_text, \
            'when user successfully registered button "Войти" is changed on "Оформить заказ"'

    def test_new_user_successfully_login_through_registration_form(self, driver):
        email = generate_username()[0] + str(random.randint(100, 999)) + '@gmail.com'
        name = email
        password = random.randint(100000, 10000000)
        print(email)

        WebDriverWait(driver, 6) \
            .until(EC.element_to_be_clickable((By.XPATH, ENTER_ACCOUNT_BUTTON))) \
            .click()
        WebDriverWait(driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, REGISTER_LINK))) \
            .click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, NAME_INPUT_ON_REGISTRATION_FORM))) \
            .send_keys(name)
        driver.find_element(By.XPATH, EMAIL_INPUT_ON_REGISTRATION_FORM).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_INPUT_ON_REGISTRATION_FORM).send_keys(password)
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        WebDriverWait(driver, 12).until(
            EC.visibility_of_element_located((By.XPATH, ENTERING_HEADER)))
        actual_text = login(driver, email, password)
        expected_text = 'Оформить заказ'
        assert actual_text == expected_text, \
            'when user successfully registered buton "Войти" is changed on "Оформить заказ"'
