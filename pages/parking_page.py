from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import os



class ParkingCalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://practice.expandtesting.com/webpark"
        # Locators
        self.parking_dropdown = (By.ID, "parkingLot")
        self.entry_date = (By.ID, "entryDate")
        self.entry_time = (By.ID, "entryTime")
        self.exit_date = (By.ID, "exitDate")
        self.exit_time = (By.ID, "exitTime")
        self.calculate_button = (By.ID, "calculateCost")
        self.result_text = (By.CSS_SELECTOR, "#result .alert-info")

    def load(self):
        self.driver.get(self.url)

    def select_parking_lot(self, parking_type):
        dropdown = self.driver.find_element(*self.parking_dropdown)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
        Select(dropdown).select_by_visible_text(parking_type)

    def set_entry_details(self, date, time):
        self.driver.execute_script("arguments[0].value = arguments[1]", self.driver.find_element(*self.entry_date), date)
        field = self.driver.find_element(*self.entry_time)
        field.clear()
        field.send_keys(time)

    def set_exit_details(self, date, time):
        self.driver.execute_script("arguments[0].value = arguments[1]", self.driver.find_element(*self.exit_date), date)
        field = self.driver.find_element(*self.exit_time)
        field.clear()
        field.send_keys(time)

    def click_calculate(self):
        btn = self.driver.find_element(*self.calculate_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        btn.click()

    def get_result_text(self):
        return self.driver.find_element(*self.result_text).text

