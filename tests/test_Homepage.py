import time

import pytest

from POM.Homepage import HomePage
from Testdata.Data_for_homepage import Homepagedata
from utilites.Baseclass import BaseClass


class TestSignupPage(BaseClass):
    def test_regrestrationform(self, getData):
        log = self.getLogger()
        h = HomePage()
        log.info("First name is "+ getData["firstname"])
        h.username(self.driver).send_keys(getData["firstname"])
        h.user_email(self.driver).send_keys(getData["email"])
        h.password(self.driver).send_keys(getData["password"])
        h.radiobutton(self.driver).click()
        h.radiobutton1(self.driver).click()
        self.selectoptionsBydropdown(h.gender(self.driver), getData["gender"])
        h.submit(self.driver).click()
        validation = h.validation_msg(self.driver).text
        log.info(validation)
        h.two_way_binding(self.driver).send_keys("success")
        time.sleep(2)
        h.clear_data(self.driver).clear()
        assert "success" in validation
        self.driver.refresh()

    @pytest.fixture(params=Homepagedata.data)
    def getData(self, request):
        return request.param
