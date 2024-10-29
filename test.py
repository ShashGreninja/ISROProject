from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the Selenium WebDriver (Chrome in this case)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://pradan.issdc.gov.in/ch2/protected/browse.xhtml?id=class")

# Wait for user to log in manually and change the view to "Download"
input("Please log in and change the view to 'Download', then press Enter to continue...")

# Initialize the starting value
start_value = 1

# Retry limit to prevent infinite loop
max_retries = 3

# Run a loop for selecting files in batches and downloading
while True:
    retry_count = 0

    # Enter the initial value in the input box
    while retry_count < max_retries:
        try:
            start_index_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "tableForm:startIndex"))
            )
            start_index_box.clear()
            start_index_box.send_keys(str(start_value))
            time.sleep(1)  # Brief delay to let the input register
            break  # Exit loop if successful
        except Exception as e:
            retry_count += 1
            print("Retrying entering the initial value due to error:", e)
    if retry_count == max_retries:
        print("Max retries reached for entering start index.")
        break

    # Re-fetch the "Select" button after input to ensure it’s fresh
    retry_count = 0
    while retry_count < max_retries:
        try:
            select_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "tableForm:selectButton"))
            )
            select_button.click()
            time.sleep(1)  # Brief delay to ensure selection
            break  # Exit loop if successful
        except Exception as e:
            retry_count += 1
            print("Retrying clicking the Select button due to error:", e)
    if retry_count == max_retries:
        print("Max retries reached for clicking Select button.")
        break

    # Click the "DOWNLOAD SELECTED as zip" button
    retry_count = 0
    while retry_count < max_retries:
        try:
            download_zip_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'DOWNLOAD SELECTED as zip')]"))
            )
            download_zip_button.click()
            print(f"Downloaded batch starting from index {start_value}.")
            break  # Exit loop if successful
        except Exception as e:
            retry_count += 1
            print("Retrying clicking Download button due to error:", e)
    if retry_count == max_retries:
        print("Max retries reached for clicking Download button.")
        break

    # Increment the start value for the next batch
    start_value += 500
