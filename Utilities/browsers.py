import pytest
from selenium import webdriver

global url, browser_type, chromedriver_path,geckodriver_path, wait_time, baseUrl

url = "https://www.demoblaze.com/"
wait_time = 15
browser_type = "Chrome"
chromedriver_path = "C:/Users/mm195/Desktop/YMLILGEE/Programs/Gecko Driver/chromedriver_win32/chromedriver.exe"
geckodriver_path = "C:/Users/mm195/Desktop/YMLILGEE/Programs/Gecko Driver/geckodriver-v0.26.0-win64/geckodriver.exe"

class Browser:

    @pytest.fixture
    def setups(self):
        if browser_type == "Chrome":
            driver = webdriver.Chrome(executable_path=chromedriver_path)
        elif browser_type == "Firefox":
            driver = webdriver.Firefox(executable_path=geckodriver_path)
        elif browser_type == "Headless Chrome":
            opts = webdriver.ChromeOptions
            opts.add_argument("headless")
            driver = webdriver.Chrome(executable_path=chromedriver_path, options=opts)
        else:
            raise Exception('Browser not supported')

        driver.implicitly_wait(wait_time)

        # Return the Browser/ Driver instance
        yield driver

        #Quit out of the browser after executions
        driver.quit()

