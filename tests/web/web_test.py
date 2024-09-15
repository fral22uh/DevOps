import pytest
from time import sleep
from assertpy import assert_that
from tests.web.test_base import WebBase
from tests.web.pages.login_page import LoginPage
from tests.web.pages.login_page import RegisterPage
from tests.web.pages.login_page import CalculatePage

class TestWeb(WebBase):

    def test_login(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        LoginPage(self.driver).elements.login.set()

        assert_that(LoginPage(self.driver).elements.username_logged_in.text).is_equal_to('admin')


class TestCalc(WebBase):

    def test_calc_add_e2e(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')

        CalculatePage(self.driver).elements.login.click()
        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyadd.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('3')

    def test_calc_sub_e2e(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')

        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key5.click()
        CalculatePage(self.driver).elements.keysubtract.click()
        CalculatePage(self.driver).elements.key3.click()
        CalculatePage(self.driver).elements.keyequals.click()

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('2')

    def test_calc_div_e2e(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')

        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key6.click()
        CalculatePage(self.driver).elements.keydivide.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('3')

    def test_calc_multi_e2e(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        
        CalculatePage(self.driver).elements.keyclear.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keymultiply.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        assert_that(CalculatePage(self.driver).elements.screen.value).is_equal_to('4')

class TestReg(WebBase):
    
    def test_register(self):
        RegisterPage(self.driver).elements.register.click()
        RegisterPage(self.driver).elements.username.set('albin')
        RegisterPage(self.driver).elements.password1.set('test1234')
        RegisterPage(self.driver).elements.password2.set('test1234')
        RegisterPage(self.driver).elements.register.click()
        
        assert_that(RegisterPage(self.driver).elements.username_registered.text).is_equal_to('User already exists!')

class TestHistory(WebBase):

    def test_calculator_history(self):
        LoginPage(self.driver).elements.username.set('admin')
        LoginPage(self.driver).elements.password.set('test1234')
        CalculatePage(self.driver).elements.login.click()

        CalculatePage(self.driver).elements.key1.click()
        CalculatePage(self.driver).elements.keyadd.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()
        CalculatePage(self.driver).elements.keyclear.click()

        CalculatePage(self.driver).elements.key6.click()
        CalculatePage(self.driver).elements.keydivide.click()
        CalculatePage(self.driver).elements.key2.click()
        CalculatePage(self.driver).elements.keyequals.click()

        CalculatePage(self.driver).elements.historybutton.click()

        assert_that(CalculatePage(self.driver).elements.historypanel.value).is_equal_to('1+2=3\n6/2=3\n')

