from selenium.webdriver.common.by import By
from tests.locators import PERSONAL_ACCOUNT, STELLA_BURGER_LABEL, HEADER_ON_MAIN_PAGE


class TestUserSeeMainPageAfterClickingOnStellarBurgersLabel:
    def test_user_see_main_page_after_clicking_on_stellar_burgers_label(self, driver, login_as_new_user):
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT).click()
        driver.find_element(By.CLASS_NAME, STELLA_BURGER_LABEL).click()
        expected_result = 'Соберите бургер'
        actual_result = driver.find_element(By.TAG_NAME, HEADER_ON_MAIN_PAGE).text
        assert actual_result == expected_result, \
            'there should be "Соберите бургер" header after clicking on stellar burgers label'
