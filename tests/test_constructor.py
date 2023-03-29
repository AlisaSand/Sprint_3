from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.locators import BAKER_TAB, BAKER_HEADER, FILLINGS_TAB, FILLINGS_HEADER, SAUCE_TAB, SAUCE_HEADER


class TestConstructor:
    def test_user_can_open_baker_section_clicking_on_it(self, driver, login_as_new_user):
        element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, BAKER_TAB)))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, BAKER_HEADER)))
        assert element.is_displayed(), 'there should be a header "Булки" in constructor section'

    def test_user_can_open_fillings_section_clicking_on_it(self, driver, login_as_new_user):
        element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, FILLINGS_TAB)))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, FILLINGS_HEADER)))
        assert element.is_displayed(), 'there should be a header "Начинки" in constructor section'

    def test_user_can_open_sauce_section_clicking_on_it(self, driver, login_as_new_user):
        element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, SAUCE_TAB)))
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, SAUCE_HEADER)))
        assert element.is_displayed(), 'there should be a header "Соусы" in constructor section'
