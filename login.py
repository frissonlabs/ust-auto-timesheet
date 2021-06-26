from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from os import getenv
from dotenv import load_dotenv

from pathlib import Path  # Python 3.6+ only
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
	sleep(0.5)
	next_button = webdriver.find_element_by_xpath('//input[@type="submit"]')
	next_button.click()

	try:
		wait.until(EC.url_contains(REDIRECT_URL), "No need to authenticate via Azure")
	except Exception as e:
		print(e)
  
	password_field = wait.until(lambda driver: driver.find_element_by_id("passwordInput"))
	password_field.send_keys(password)

	submit_button = webdriver.find_element_by_id("submitButton")
	submit_button.click()

	diff_options_link = wait.until(lambda driver: driver.find_element_by_id("differentVerificationOption"))
	diff_options_link.click()

	sec_questions_link = webdriver.find_element_by_id("verificationOption2")
	sec_questions_link.click()

	q1 = webdriver.find_element_by_id("question1")
	key1 = q1.text.upper().replace(" ", "_").replace("'", "").replace("?", "")
	a1_input = webdriver.find_element_by_id("answer1Input")
	a1_input.send_keys(getenv(key1))

	q2 = webdriver.find_element_by_id("question2")
	key2 = q2.text.upper().replace(" ", "_").replace("'", "").replace("?", "")
	a2_input = webdriver.find_element_by_id("answer2Input")
	a2_input.send_keys(getenv(key2))

	authenticate_button = webdriver.find_element_by_id("authenticateButton")
	authenticate_button.click()
 
	return wait.until(EC.url_matches("https://usttimesheet.azurewebsites.net/timesheet"))

		
