import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logfiles = logging.FileHandler(r'C:\Users\pbudaraju\PycharmProjects\Frameworkpratice\utilites\framework.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        logfiles.setFormatter(formatter)
        logger.addHandler(logfiles)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifylinks(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoptionsBydropdown(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)
