import allure
from pages.login_page import LoginPage

URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@allure.title("Verify user can login successfully")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_valid(driver):
    with allure.step("Open Login Page"):
        driver.get(URL)

    login = LoginPage(driver)

    with allure.step("Enter Username"):
        login.enter_username("Admin")

    with allure.step("Enter Password"):
        login.enter_password("admin123")

    with allure.step("Click Login"):
        login.click_login()

    with allure.step("Verify Login Successful"):
        assert login.is_logged_in()


@allure.title("Verify login fails with invalid password")
@allure.severity(allure.severity_level.NORMAL)
def test_login_invalid_password(driver):
    driver.get(URL)
    login = LoginPage(driver)

    login.enter_username("Admin")
    login.enter_password("wrongpass")
    login.click_login()

    assert "Invalid credentials" in login.get_banner_error()


@allure.title("Verify login fails with invalid username")
@allure.severity(allure.severity_level.NORMAL)
def test_login_invalid_username(driver):
    driver.get(URL)
    login = LoginPage(driver)

    login.enter_username("WrongUser")
    login.enter_password("admin123")
    login.click_login()

    assert "Invalid credentials" in login.get_banner_error()


@allure.title("Verify login fails when username and password are blank")
@allure.severity(allure.severity_level.MINOR)
def test_login_blank_fields(driver):
    driver.get(URL)
    login = LoginPage(driver)

    login.enter_username("")
    login.enter_password("")
    login.click_login()

    # Field-level validation messages
    assert "Required" in login.get_username_error()
    assert "Required" in login.get_password_error()
