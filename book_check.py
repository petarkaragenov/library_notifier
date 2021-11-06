from win10toast import ToastNotifier
import webbrowser
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from book_dates import BookDates
from const import LIB_URL, USER, PASS

class BookCheck(webdriver.Chrome):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.get(LIB_URL)
        sleep(5)
        try:
            username = self.find_element(By.ID, 'username')
            password = self.find_element(By.ID, 'password')
            submit = self.find_element(By.XPATH, '//*[@id="tl_login"]/div/div[3]/input')
        except NoSuchElementException:
            pass
        else:
            username.send_keys(USER)
            sleep(1)
            password.send_keys(PASS)
            sleep(1)
            submit.click()

        sleep(5)

        books = self.find_elements(By.CLASS_NAME, "loans-actions-info")
        dates = [book.find_element(By.TAG_NAME, "strong").text for book in books]
        
        book_dates = BookDates(dates)
        warning = book_dates.make_warning()  
        self.warn_me(warning)

        if "today" in warning:
            self.open_browser()

        self.quit()

    def warn_me(self, warning):
        toast = ToastNotifier()
        toast.show_toast("Library Notifier", warning, duration=10)

    def open_browser(self):
        webbrowser.open(LIB_URL, new=2)
