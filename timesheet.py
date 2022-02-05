from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

days = ["mon", "tue", "wed", "thu", "fri"]


def fill_timesheet(webdriver, project_id, project_task, is_billable=True) -> None:
	try:
		wait = WebDriverWait(webdriver, 10)
		sleep(2)
		workdays = [day for day in days if float(webdriver.find_element_by_xpath(
			"//a[@href='#" + day + "']").find_elements_by_tag_name("small")[-1].text) == 0]

		for day in workdays:
			webdriver.find_element_by_xpath("//a[@href='#" + day + "']").click()

			webdriver.find_element_by_xpath(
				"//i[@class='fa fa-plus text-light']").find_element_by_xpath('..').click()
			wait.until(lambda x: x.find_element_by_id(
				"newTimeModal").is_displayed())

			project_select_el = wait.until(lambda x: x.find_element_by_xpath(
				"//label[contains(text(), 'Project Name')]/following-sibling::select"))
			project_select = Select(
				project_select_el).select_by_value(project_id)

			Select(wait.until(lambda x: x.find_element_by_xpath(
				"//label[contains(text(), 'Task Name')]/following-sibling::select"))).select_by_value('0')
			Select(webdriver.find_element_by_xpath(
				"//label[contains(text(), 'Work Location')]/following-sibling::select")).select_by_value('WFH')
			wait.until(lambda x: x.find_element_by_xpath(
				"//label[contains(text(), 'End')]/following-sibling::input")).click()
			sleep(1)
			wait.until(lambda x: x.find_element_by_xpath(
				"//button[@aria-label='Minus a hour']")).click()
			sleep(1)
			wait.until(lambda x: x.find_element_by_xpath(
				"//span[contains(text(), 'Set')]")).find_element_by_xpath('..').click()

			webdriver.find_element_by_xpath(
				"//button[contains(text(), 'Add')]").click()
	except Exception:
		print("exception")

def submit_timesheet(webdriver) -> None:
    webdriver.find_element_by_xpath(
        "//button[contains(text(), 'Submit')]").click()
    webdriver.switch_to.alert.accept()


def get_timesheet_date_range(webdriver) -> str:
    try:
        date_range: WebElement = WebDriverWait(webdriver, 30).until(
            lambda x: x.find_element_by_class_name("dtnWeek")
        )
        return date_range.text
    except Exception:
        return "?"
