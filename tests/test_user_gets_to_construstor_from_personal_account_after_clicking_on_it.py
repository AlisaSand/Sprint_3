from selenium.webdriver.common.by import By
from tests.locators import PERSONAL_ACCOUNT, CONSTRUCTOR_LINK, HEADER_ON_MAIN_PAGE


class TestUserGetsToConstructorFromPersonalAccountAfterClickingOnIt:
    def test_user_gets_to_constructor_from_personal_account_after_clicking_on_it(self, driver, login_as_new_user):
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT).click()
        driver.find_element(By.XPATH, CONSTRUCTOR_LINK).click()
        expected_result = 'Соберите бургер'
        actual_result = driver.find_element(By.TAG_NAME, HEADER_ON_MAIN_PAGE).text
        assert actual_result == expected_result, \
            'there should be "Соберите бургер" header after clicking on constructor'
