from time import sleep
from selenium.webdriver.common.by import By
from POM.Confirmpage import ConfirmPage
from POM.Homepage import HomePage
from utilites.Baseclass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage()
        cartpage = homePage.shopItems(self.driver)
        products = cartpage.getCardTitles(self.driver)
        log.info(products)
        for product in products:
            name = product.find_element(By.XPATH, "div/h4/a").text
            if name == 'iphone X':
                cartpage.getCardFooter(self.driver).click()
        sleep(3)
        self.driver.execute_script("window.scrollBy(0,-250);")
        sleep(3)
        cartpage.button(self.driver).click()
        cartpage.cartcheckout(self.driver).click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifylinks("India")
        cartpage.dropdownoptions(self.driver).click()
        confirmationpage = ConfirmPage()
        confirmationpage.purchase(self.driver).click()
        confirmationpage.proceedcheckout(self.driver).click()
        msg = confirmationpage.finalmsg(self.driver).text
        log.info("Text recived from application is"+ msg)
        assert "Success! Thank you!" in msg
