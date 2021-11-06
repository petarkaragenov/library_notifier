from book_check import BookCheck
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from const import CHROME_DRIVER

service = Service(executable_path=CHROME_DRIVER)
chrome_options = Options()
chrome_options.add_argument("--headless")

BookCheck(service=service, chrome_options=chrome_options)
