from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import BaseCase


class LoginPage(BaseCase):
    username_txt_id = "#loginusername"
    password_txt_id = "#loginpassword"
    login_lnk_xpath = "[data-target='#logInModal']"
    login_btn_css = "[onclick='logIn()']"
    logout_lnk_css ="[onclick='logOut()']"
    signup_lnk_css = "[data-target='#signInModal']"
    cart_lnk_css = "#cartur"


    close_btn_xpath = "//div[@id='logInModal']//button[@class='btn btn-secondary']"
    loginUsername_id = "nameofuser"
    samsung_linktext = "//a[.='Nokia lumia 1520']"
    addtocart_xpath = "Add to cart"
    placeorder_xpath = "//button[@class='btn btn-success']"
    cart_xpath = "//a[.='Cart']"

    url = "https://www.demoblaze.com/"
    email = "itsforme60@gmail.com"
    password = "ymlilgee1991"
    invalid_email = "itsforme60@gmail.com"
    invalid_password = "ymlilgee1992"


    def login_valid_details(self):
        self.open(self.url)
        self.click(self.login_lnk_xpath)
        self.type(self.username_txt_id,self.email)
        self.type(self.password_txt_id,self.password)
        self.click(self.login_btn_css)
        #self.assert_text("Welcome itsforme60@gmail.com","#nameofuser", timeout=15)

    def login_invalid_details(self):
        self.open(self.url)
        self.click(self.login_lnk_xpath)
        self.type(self.username_txt_id,self.email)
        self.type(self.password_txt_id,self.invalid_password)
        self.click(self.login_btn_css)
        self.switch_to_alert()

    def logout(self):
        self.click(self.logout_lnk_css)














    # def __init__(self,driver):
    #     self.driver = driver
    #     wait = WebDriverWait(driver, 10)
    #
    # def clickLoginLink(self):
    #     browser = self.driver
    #     browser.find_element(By.XPATH, self.login_lnk_xpath).click()
    #
    # def setUsername(self,username):
    #     browser = self.driver
    #     browser.find_element(By.ID, self.username_txt_id).clear()
    #     browser.find_element(By.ID, self.username_txt_id).send_keys(username)
    #
    # def setPassword(self,password):
    #     browser = self.driver
    #     browser.find_element(By.ID, self.password_txt_id).clear()
    #     browser.find_element(By.ID, self.password_txt_id).send_keys(password)
    #
    # def clickLoginButton(self):
    #     browser = self.driver
    #     browser.find_element(By.XPATH, self.login_btn_xpath).click()
    #
    # def clckCloseButton(self):
    #     browser = self.driver
    #     browser.find_element(By.XPATH, self.close_btn_xpath).click()
    #
    # def getUsername(self):
    #     browser = self.driver
    #     loginname = browser.find_element(By.ID, self.loginUsername_id)
    #     return loginname
    #
    # ## Other Methods
    # def clickSamsung(self):
    #     browser = self.driver
    #     browser.find_element(By.XPATH, self.samsung_linktext).click()
    #
    # def clickAddtoCart(self):
    #     browser = self.driver
    #     browser.find_element(By.LINK_TEXT, self.addtocart_xpath).click()
    #     #self.wait.until(ec.presence_of_element_located(By.ID, self.addtocart_xpath))
    #
    # def clickOnPlaceOrder(self):
    #     browser = self.driver
    #     browser.find_element(By.XPATH, self.placeorder_xpath).click()
    #
    # def clickOnCart(self):
    #     browser = self.driver
    #     browser.find_element(By.XPATH, self.cart_xpath).click()


