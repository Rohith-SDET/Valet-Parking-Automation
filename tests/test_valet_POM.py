import sys
import os
import pytest
import time
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.parking_page import ParkingCalculatorPage


@pytest.mark.parametrize("parking_type, entry_date, entry_time, exit_date, exit_time", [
    ("Valet Parking", "2025-06-22", "10:00AM", "2025-06-23", "10:00AM"),
    ("Short-Term Parking", "2025-06-22", "09:00AM", "2025-06-23", "02:30AM"),
    ("Long-Term Garage Parking", "2025-06-21", "08:00AM", "2025-06-28", "08:00AM"),
    ("Long-Term Surface Parking", "2025-06-20", "06:00AM", "2025-06-27", "06:00AM"),
    ("Economy Parking", "2025-06-19", "07:30AM", "2025-06-26", "07:30AM"),
])
def test_parking_cost(parking_type, entry_date, entry_time, exit_date, exit_time):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()

    page = ParkingCalculatorPage(driver)
    page.load()
    page.select_parking_lot(parking_type)
    page.set_entry_details(entry_date, entry_time)
    page.set_exit_details(exit_date, exit_time)
    page.click_calculate()

    time.sleep(1)  # Optional: ensure the result is fully rendered
    result = page.get_result_text()

    print(f"\n--- {parking_type} ---")
    print("Entry: ", entry_date, entry_time)
    print("Exit: ", exit_date, exit_time)
    print("Cost: ", result)
