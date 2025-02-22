# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# from utilities.customLogger import LogGen
#
# class BasePage:
#     def __init__(self, driver, logger=None):
#         self.driver = driver
#         self.logger = logger
#         self.wait = WebDriverWait(driver, 60)
#         self.action = ActionChains(driver)
#         logger = LogGen.loggen()
#
#     def click(self, element, element_name="Element"):
#         element.click()
#         print(f"{element_name} is clicked")
#         self.logger.info(f"{element_name} is clicked")
#
#     def click_using_js(self, element, element_name="Element"):
#         self.driver.execute_script("arguments[0].click();", element)
#         print(f"{element_name} is clicked using JavaScript")
#         self.logger.info(f"{element_name} is clicked")
#
#     def send_keys(self, element, value, element_name="Element"):
#         element.send_keys(value)
#         print(f"{value} is entered successfully in {element_name} field")
#
#     def select_dropdown_by_visible_text(self, element, value, dropdown_name="Dropdown"):
#         Select(element).select_by_visible_text(value)
#         print(f"{value} is selected from the {dropdown_name} dropdown")
#
#     def select_dropdown_by_value(self, element, value, dropdown_name="Dropdown"):
#         Select(element).select_by_value(value)
#         print(f"{value} is selected from the {dropdown_name} dropdown")
#
#     def mouse_over(self, element):
#         self.action.move_to_element(element).perform()
#         print("Mouse hovered over element")
#
#     def get_text(self, element, field_name="Element"):
#         text = element.text.strip()
#         print(f"{text} text found in {field_name} field")
#         return text
#
#     def scroll_into_view(self, element):
#         self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
#
#     def wait_for_visibility(self, locator):
#         return self.wait.until(EC.visibility_of_element_located(locator))
#
#     def wait_for_clickable(self, locator):
#         return self.wait.until(EC.element_to_be_clickable(locator))
#
#     def wait_for_presence(self, locator):
#         return self.wait.until(EC.presence_of_element_located(locator))
#
#     def wait_for_invisibility(self, locator):
#         return self.wait.until(EC.invisibility_of_element_located(locator))
#
#     def wait_for_frame_and_switch(self, element):
#         return self.wait.until(EC.frame_to_be_available_and_switch_to_it(element))
#
#     def select_custom_dropdown(self, dropdown_locator, options_locator, value):
#         self.driver.find_element(*dropdown_locator).click()
#         options = self.driver.find_elements(*options_locator)
#         for option in options:
#             if option.text == value:
#                 option.click()
#                 break














import logging
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.customLogger import LogGen

class BasePage:
    def __init__(self, driver, logger=None):
        self.driver = driver
        self.logger = logger if logger else LogGen.loggen()
        self.wait = WebDriverWait(driver, 60)
        self.action = ActionChains(driver)

    def attach_screenshot_to_report(self, name="screenshot"):
        """Capture a screenshot and attach it directly to the Allure report (without saving locally)."""
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        self.logger.info(f"Screenshot captured and attached to report: {name}")

    def click(self, element, element_name="Element"):
        """Click an element, log action, and attach screenshot to Allure."""
        try:
            element.click()
            self.logger.info(f"{element_name} clicked.")
            allure.attach(f"{element_name} clicked.", name=element_name, attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{element_name}_clicked")
        except Exception as e:
            self.logger.error(f"Failed to click {element_name}: {str(e)}")
            allure.attach(f"Failed to click {element_name}: {str(e)}", name="Error Log", attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{element_name}_click_failed")
            raise

    def send_keys(self, element, value, element_name="Element"):
        """Enter text in an element, log action, and attach screenshot."""
        try:
            element.send_keys(value)
            self.logger.info(f"Entered '{value}' in {element_name}.")
            allure.attach(f"Entered '{value}' in {element_name}.", name=element_name, attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{element_name}_input")
        except Exception as e:
            self.logger.error(f"Failed to enter '{value}' in {element_name}: {str(e)}")
            allure.attach(f"Failed to enter '{value}' in {element_name}: {str(e)}", name="Error Log", attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{element_name}_input_failed")
            raise

    def select_dropdown_by_visible_text(self, element, value, dropdown_name="Dropdown"):
        """Select a dropdown option and attach a screenshot."""
        try:
            Select(element).select_by_visible_text(value)
            self.logger.info(f"Selected '{value}' from {dropdown_name}.")
            allure.attach(f"Selected '{value}' from {dropdown_name}.", name=dropdown_name, attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{dropdown_name}_selected_{value}")
        except Exception as e:
            self.logger.error(f"Failed to select '{value}' from {dropdown_name}: {str(e)}")
            allure.attach(f"Failed to select '{value}' from {dropdown_name}: {str(e)}", name="Error Log", attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{dropdown_name}_selection_failed")
            raise

    def mouse_over(self, element, element_name="Element"):
        """Perform mouse hover action and attach screenshot."""
        try:
            self.action.move_to_element(element).perform()
            self.logger.info(f"Mouse hovered over {element_name}.")
            allure.attach(f"Mouse hovered over {element_name}.", name=element_name, attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{element_name}_hovered")
        except Exception as e:
            self.logger.error(f"Failed to hover over {element_name}: {str(e)}")
            allure.attach(f"Failed to hover over {element_name}: {str(e)}", name="Error Log", attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{element_name}_hover_failed")
            raise

    def get_text(self, element, field_name="Element"):
        """Get text from an element and attach screenshot."""
        try:
            text = element.text.strip()
            self.logger.info(f"Retrieved text '{text}' from {field_name}.")
            allure.attach(f"Retrieved text '{text}' from {field_name}.", name=field_name, attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{field_name}_text")
            return text
        except Exception as e:
            self.logger.error(f"Failed to retrieve text from {field_name}: {str(e)}")
            allure.attach(f"Failed to retrieve text from {field_name}: {str(e)}", name="Error Log", attachment_type=allure.attachment_type.TEXT)
            self.attach_screenshot_to_report(f"{field_name}_text_failed")
            raise

    def wait_for_visibility(self, locator):
        """Wait until an element is visible."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """Wait until an element is clickable."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        """Wait until an element is present in the DOM."""
        return self.wait.until(EC.presence_of_element_located(locator))
