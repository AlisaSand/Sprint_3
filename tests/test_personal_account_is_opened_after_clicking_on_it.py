from selenium.webdriver.common.by import By
from tests.locators import PERSONAL_ACCOUNT, PROFILE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPersonalAccountIsOpenedAfterClickingOnIt:
    def test_personal_account_is_opened_after_clicking_on_it(self, driver, login_as_new_user):
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT).click()
        actual_result = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, PROFILE))) \
            .text
        expected_result = 'Профиль'
        assert actual_result == expected_result, 'There should be a profile settings'
