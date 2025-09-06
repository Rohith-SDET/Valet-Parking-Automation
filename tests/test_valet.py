import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def calculate_expected_cost(parking_type, hours):
    if parking_type == "Valet Parking":
        return "12.00€" if hours <= 5 else "18.00€"
    elif parking_type == "Short-Term Parking":
        cost = 2.00
        hours -= 1
        cost += (hours * 2)
        return f"{min(cost, 24.00):.2f}€"
    elif parking_type == "Long-Term Garage Parking":
        days = hours / 24
        weeks = int(days / 7)
        rem_days = days % 7
        cost = (weeks * 72) + min(12 * rem_days, 72)
        return f"{cost:.2f}€"
    elif parking_type == "Long-Term Surface Parking":
        days = hours / 24
        weeks = int(days / 7)
        rem_days = days % 7
        cost = (weeks * 60) + min(10 * rem_days, 60)
        return f"{cost:.2f}€"
    elif parking_type == "Economy Parking":
        days = hours / 24
        weeks = int(days / 7)
        rem_days = days % 7
        cost = (weeks * 54) + min(9 * rem_days, 54)
        return f"{cost:.2f}€"



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

    driver.get("https://practice.expandtesting.com/webpark")

    # Select parking type from dropdown
    dropdown = driver.find_element(By.ID, "parkingLot")
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    select = Select(dropdown)
    select.select_by_visible_text(parking_type)

    # Fill Entry Date
    entry_date_input = driver.find_element(By.ID, "entryDate")
    driver.execute_script("arguments[0].value = arguments[1]", entry_date_input, entry_date)

    # Fill Entry Time
    entry_time_input = driver.find_element(By.ID, "entryTime")
    entry_time_input.clear()
    entry_time_input.send_keys(entry_time)

    # Fill Exit Date
    exit_date_input = driver.find_element(By.ID, "exitDate")
    driver.execute_script("arguments[0].value = arguments[1]", exit_date_input, exit_date)

    # Fill Exit Time
    exit_time_input = driver.find_element(By.ID, "exitTime")
    exit_time_input.clear()
    exit_time_input.send_keys(exit_time)

    # Click Calculate
    driver.find_element(By.ID, "calculateCost").click()

    time.sleep(1)

    # Get Result
    result = driver.find_element(By.CSS_SELECTOR, "#result .alert-info").text
    print(f"\n--- {parking_type} ---")
    print("Entry: ", entry_date, entry_time)
    print("Exit: ", exit_date, exit_time)
    print("Cost: ", result)

    driver.quit()
