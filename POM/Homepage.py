from selenium.webdriver.common.by import By

from POM.Checkoutpage import CheckOutPage


class HomePage:
    def __int__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*= 'shop']")
    name = (By.CSS_SELECTOR, "input[name = 'name']")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    button = (By.CSS_SELECTOR, "#inlineRadio1")
    button1 = (By.ID, "exampleCheck1")
    gender_dd = (By.ID, "exampleFormControlSelect1")
    confirm = (By.XPATH, "//input[@type = 'submit']")
    msg = (By.CLASS_NAME, "alert-success")
    databinding = (By.XPATH, "(//input[@type = 'text'])[3]")
    clearing =  (By.XPATH, "(//input[@type = 'text'])[3]")

    def shopItems(self, driver):
        driver.find_element(*HomePage.shop).click()
        cartpage = CheckOutPage()
        return cartpage

    def username(self, driver):
        return driver.find_element(*HomePage.name)

    def user_email(self, driver):
        return driver.find_element(*HomePage.email)

    def password(self, driver):
        return driver.find_element(*HomePage.pwd)

    def radiobutton(self, driver):
        return driver.find_element(*HomePage.button)

    def radiobutton1(self, driver):
        return driver.find_element(*HomePage.button1)

    def gender(self, driver):
        return driver.find_element(*HomePage.gender_dd)

    def submit(self, driver):
        return driver.find_element(*HomePage.confirm)

    def validation_msg(self, driver):
        return driver.find_element(*HomePage.msg)

    def two_way_binding(self, driver):
        return driver.find_element(*HomePage.databinding)

    def clear_data(self, driver):
        return driver.find_element(*HomePage.clearing)
