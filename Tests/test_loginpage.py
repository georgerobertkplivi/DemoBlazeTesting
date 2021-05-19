from Pages.LoginPage import LoginPage


class TestLoginPage(LoginPage):


    def test_login_valid_details(self):
        self.login_valid_details()
        self.assert_element(self.logout_lnk_css)
        self.assert_text("Welcome itsforme60@gmail.com","#nameofuser", timeout=15)
        self.logout()

    def test_login_invalid_details(self):
        self.login_invalid_details()
        self.accept_alert()



    # def test_login(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.loggs.info("*** Starting Test  ***")
    #     self.login = LoginPage(self.driver)
    #     self.login.clickLoginLink()
    #     self.login.setUsername(self.email)
    #     self.login.setPassword(self.password)
    #     self.login.clickLoginButton()
    #     try:
    #         self.login.getUsername()
    #     except:
    #         print("Element not visible")
    #     self.loggs.info("***  End Test ***")


    # def test_placeorder(self,setup):
    #     self.driver = setup
    #     self.driver.get(self.url)
    #     self.login = LoginPage(self.driver)
    #     self.login.clickLoginLink()
    #     self.login.setUsername(self.email)
    #     self.login.setPassword(self.password)
    #     self.login.clickLoginButton()
    #     try:
    #         self.login.getUsername()
    #     except:
    #         print("Element not visible")

        #self.login.clickSamsung()
        # try:
        #     self.login.addtocart_xpath
        # except:
        #     print('Element not found'
        # time.sleep(10)
        #self.login.clickAddtoCart()
        # self.login.clickOnCart()
        # self.login.clickOnPlaceOrder()

