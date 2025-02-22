import pytest
from selenium import webdriver

class BaseTest:
    driver = None  # Class-level driver variable

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Fixture to initialize and quit the WebDriver before and after each test."""
        self.init_driver()
        yield  # This pauses execution here until the test completes
        self.quit_driver()

    @classmethod
    def init_driver(cls):
        """Initialize the WebDriver."""
        cls.driver = webdriver.Chrome()  # Change to desired driver (e.g., Firefox, Edge)
        cls.driver.maximize_window()

    @classmethod
    def quit_driver(cls):
        """Quit the WebDriver."""
        if cls.driver:
            cls.driver.quit()
