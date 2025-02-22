# from selenium.webdriver.common.by import By
#
# from pageObjects.basePage import BasePage
#
#
# class LoginPage(BasePage):
#     # Login Page
#     textbox_username_id = "Email"
#     textbox_password_id = "Password"
#     button_login_xpath = "//button[text()='Log in']"
#     link_logout_linktext = "Logout"
#
#     def __init__(self,driver):
#         self.driver=driver
#
#     def setUserName(self, username):
#         self.driver.find_element(By.ID,self.textbox_username_id).clear()
#         self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
#
#     def setPassword(self, password):
#         self.driver.find_element(By.ID,self.textbox_password_id).clear()
#         self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
#
#     def clickLogin(self):
#         self.driver.find_element(By.XPATH,self.button_login_xpath).click()
#
#     def clickLogout(self):
#         self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()



from selenium.webdriver.common.by import By
from pageObjects.basePage import BasePage


class LoginPage(BasePage):
    # Login Page Locators
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    link_logout_linktext = "Logout"

    def __init__(self, driver, logger):
        super().__init__(driver, logger)

    def setUserName(self, username):
        element = self.driver.find_element(By.ID, self.textbox_username_id)
        self.wait_for_presence((By.ID, self.textbox_username_id))
        element.clear()
        self.send_keys(element, username, "Username Field")

    def setPassword(self, password):
        element = self.driver.find_element(By.ID, self.textbox_password_id)
        self.send_keys(element, password, "Password Field")

    def clickLogin(self):
        element = self.driver.find_element(By.XPATH, self.button_login_xpath)
        self.click(element, "Login Button")

    def clickLogout(self):
        element = self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext)
        self.click(element, "Logout Link")
