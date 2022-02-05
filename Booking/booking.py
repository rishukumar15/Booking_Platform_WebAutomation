import os
from selenium import webdriver
from Booking.booking_filtration import BookingFiltration
from Booking.booking_report import BookingReport
from prettytable import PrettyTable
import Booking.constants as const

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDriver\chromedriver_win32",teardown=False):

        self.driver_path = driver_path

        self.teardown = teardown

        os.environ['PATH'] += self.driver_path

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])        

        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()


    def __exit__(self, exc_type, exc_vlue, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):

        self.get(const.BASE_URL)
    

    def change_currency(self, currency=None):

        curreny_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )

        curreny_element.click()

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )

        selected_currency_element.click()

    def select_placeto_go(self, place_to_go):

        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )

        first_result.click()

    
    def select_dates(self, check_in_date, check_out_date):

        checkin_date_field = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )

        checkin_date_field.click()

        checkout_date_field = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )

        checkout_date_field.click()
    

    def select_adults(self, count=2):

        label_field = self.find_element_by_id('xp__guests__toggle')
        label_field.click()

        while True:

            decreased_button = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )

            decreased_button.click()

            label_value_element = self.find_element_by_id('group_adults')
            adults_value = label_value_element.get_attribute('value')

            if adults_value == "1":
                break


        for i in range(1, count):

            increased_button = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Adults"]'
            )

            increased_button.click()
    


    def select_rooms(self, room_count=1):

        for i in range(1, room_count):

            increased_button = self.find_element_by_css_selector(
                'button[aria-label="Increase number of Rooms"]'
            )

            increased_button.click()


    def search(self):

        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )

        search_button.click()
    
    def apply_filtrations(self):

        filtration = BookingFiltration(driver=self)
        
        filtration.sort_price_low()

        filtration.apply_star_rating(3, 4, 5)

        filtration.budget_filtration(int(input('Your Budget ?')))

        filtration.close_from_center_filter()
    

    def report_results(self):

        deals_return = self.find_element_by_id('search_results_table')
        
        report = BookingReport(deals_return)

        table = PrettyTable(
            field_names=["Hotel Name", "Price in INR", "Rating out of 10"]
        )

        table.add_rows(report.pull_titles())

        print(table)

    