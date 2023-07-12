from selenium.webdriver.common.by import By


class ConfirmPage:
    def __int__(self, driver):
        self.driver = driver

    buy = (By.XPATH, "//input[@value='Purchase']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    successmsg = (By.CLASS_NAME, "alert-success")

    def purchase(self, driver):
        return driver.find_element(*ConfirmPage.buy)

    def proceedcheckout(self, driver):
        return driver.find_element(*ConfirmPage.submit)

    def finalmsg(self, driver):
        return driver.find_element(*ConfirmPage.successmsg)
