import pytest
from selenium import webdriver
from enums.readProperty import ConfigSection, CredentialsOption
from utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

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
        browser = ReadConfig.getProperty(ConfigSection.CREDENTIALS, CredentialsOption.BROWSER)

        if browser == 'chrome':
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-web-security")
            chrome_options.add_argument("--allow-running-insecure-content")
            chrome_options.add_argument("--disable-popup-blocking")
            cls.driver = webdriver.Chrome(options=chrome_options)  # ✅ Assign to cls.driver
            print("✅ Launching Chrome browser...")

        elif browser == 'firefox':
            firefox_options = FirefoxOptions()
            firefox_options.set_preference("network.stricttransportsecurity.preloadlist", False)
            firefox_options.set_preference("security.insecure_field_warning.contextual.enabled", False)
            firefox_options.set_preference("webdriver_accept_untrusted_certs", True)
            cls.driver = webdriver.Firefox(options=firefox_options)  # ✅ Assign to cls.driver
            print("✅ Launching Firefox browser...")

        elif browser == 'edge':
            edge_options = EdgeOptions()
            edge_options.add_argument("--ignore-certificate-errors")
            cls.driver = webdriver.Edge(options=edge_options)  # ✅ Assign to cls.driver
            print("✅ Launching Edge browser...")

        else:
            raise ValueError("❌ Unsupported browser: Use 'chrome', 'firefox', or 'edge'.")

        cls.driver.maximize_window()  # Maximize the browser window

    @classmethod
    def quit_driver(cls):
        """Quit the WebDriver."""
        if cls.driver:
            cls.driver.quit()
            print("✅ WebDriver session closed.")
