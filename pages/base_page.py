from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_url(self, expected_url):
        self.wait.until(EC.url_to_be(expected_url))

    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url


    def find_and_wait_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
            )


    def click_button(self, locator):
        self.find_and_wait_locator(locator).click()


    def send_keys_to_field(self, locator, text):
        self.find_and_wait_locator(locator).send_keys(text)


    def get_text_locator(self, locator):
        return self.find_and_wait_locator(locator).text


    def scroll_to_locator(self, locator):
        element = self.find_and_wait_locator(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element(self, locator):
        return self.find_and_wait_locator(locator).is_displayed()