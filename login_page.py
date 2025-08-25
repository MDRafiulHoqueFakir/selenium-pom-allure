from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button   = (By.XPATH, "//button[@type='submit']")
        self.profile_icon   = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
        self.error_banner   = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
        self.forgot_password_link = (By.LINK_TEXT, "Forgot your password?")

        # Field-level errors for blank validation
        self.username_required = (
            By.XPATH,
            "//input[@name='username']/following::span[contains(@class,'oxd-input-field-error-message')][1]"
        )
        self.password_required = (
            By.XPATH,
            "//input[@name='password']/following::span[contains(@class,'oxd-input-field-error-message')][1]"
        )

    # Actions
    def enter_username(self, username: str):
        el = self.wait.until(EC.visibility_of_element_located(self.username_input))
        el.clear()
        el.send_keys(username)

    def enter_password(self, password: str):
        el = self.wait.until(EC.visibility_of_element_located(self.password_input))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        el = self.wait.until(EC.element_to_be_clickable(self.login_button))
        el.click()

    def is_logged_in(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.profile_icon)).is_displayed()

    def get_banner_error(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.error_banner)).text

    def get_username_error(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.username_required)).text

    def get_password_error(self) -> str:
        return self.wait.until(EC.visibility_of_element_located(self.password_required)).text

    def click_forgot_password(self):
        self.wait.until(EC.element_to_be_clickable(self.forgot_password_link)).click()
