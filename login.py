from os import getenv
from pathlib import Path  # Python 3.6+ only
from time import sleep

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

LOGIN_ID = "ContentPlaceHolder1_MFALoginControl1_UserIDView_txtUserid"
PASSWORD_ID = "ContentPlaceHolder1_MFALoginControl1_UserIDView_tbxPassword"
LOGIN_BUTTON_ID = "ContentPlaceHolder1_MFALoginControl1_UserIDView_btnSubmit"
REDIRECT_URL = "https://idp.ust-global.com/"

def handle_login_page(webdriver: WebDriver, url, username, password, one_time_passcode = None) -> None:
	webdriver.get(url)

	wait = WebDriverWait(webdriver, 30)
 
	try:
		wait.until(EC.url_contains(
			"https://login.microsoftonline.com/"), "No need to authenticate via Azure")
	except Exception as e:
		print(e)

	login_field = wait.until(lambda driver: driver.find_element_by_xpath('//input[@type="email"]'))

	if not login_field.text:
		login_field.send_keys(username)

	next_button = wait.until(lambda driver: driver.find_element_by_xpath('//input[@type="submit"]'))
	next_button.click()

	try:
		wait.until(EC.url_contains(REDIRECT_URL), "No need to authenticate via Azure")
	except Exception as e:
		print(e)
  
	password_field = wait.until(lambda driver: driver.find_element_by_id("passwordInput"))
	password_field.send_keys(password)

	sleep(1)

	submit_button = wait.until(lambda driver: driver.find_element_by_id("submitButton"))
	submit_button.click()

	return wait.until(EC.url_matches("https://usttimesheet.azurewebsites.net/timesheet"))

		
