from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import PERSONAL_ACCOUNT, EXIT_ACCOUNT_BUTTON, ENTERING_HEADER


class TestUserCanSuccessfullyExitAccount:
    def test_user_can_successfully_exit_account(self, driver, login_as_new_user):
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, PERSONAL_ACCOUNT))) \
            .click()
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, EXIT_ACCOUNT_BUTTON))) \
            .click()
        expected_result = 'Вход'
        actual_result = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, ENTERING_HEADER))) \
            .text
        assert actual_result == expected_result, 'entering form appeared when user exit from account'
