




import allure
import pytest
from enums.readProperty import ConfigSection, CredentialsOption
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from testCases.baseTest import BaseTest  # Import BaseTest class

@allure.feature("Login Functionality")
class Test_001_Login(BaseTest):  # Inherit from BaseTest
    baseURL = ReadConfig.getProperty(ConfigSection.CREDENTIALS, CredentialsOption.BASE_URL)
    username = ReadConfig.getProperty(ConfigSection.CREDENTIALS, CredentialsOption.USERNAME)
    password = ReadConfig.getProperty(ConfigSection.CREDENTIALS, CredentialsOption.PASSWORD)
    logger = LogGen.loggen()

    @allure.story("Verify Home Page Title")
    @allure.description("This test verifies that the home page title is displayed correctly when the user accesses the website.")
    def test_homePageTitle(self):
        """Test case for home page title."""
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "nopCommerce demo store. Login":
            assert True
        else:
            assert False

    @allure.story("User Login Test")
    @allure.description("This test verifies that the user is able to log in with valid credentials and lands on the dashboard.")
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        """Test case for user login."""
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver, self.logger)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
