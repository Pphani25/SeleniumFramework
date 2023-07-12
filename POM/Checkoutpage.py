from selenium.webdriver.common.by import By


class CheckOutPage:
    def __int__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class = 'card h-100']")
    cardFooter = (By.XPATH, "(//button[@class='btn btn-info'])[1]")
    proceedbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    successbutton = (By.XPATH, "//button[@class = 'btn btn-success']")
    dropdown = (By.LINK_TEXT , "India")
    buy = (By.XPATH, "//input[@value='Purchase']")
    submit = (By.CSS_SELECTOR, "[type='submit']")
    successmsg = (By.CLASS_NAME, "alert-success")

    def getCardTitles(self, driver):
        return driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self, driver):
        return driver.find_element(*CheckOutPage.cardFooter)

    def button(self, driver):
        return driver.find_element(*CheckOutPage.proceedbutton)

    def cartcheckout(self, driver):
        return driver.find_element(*CheckOutPage.successbutton)

    def dropdownoptions(self, driver):
        return driver.find_element(*CheckOutPage.dropdown)

