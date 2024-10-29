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

# Run an unlimited loop for selecting files in batches and downloading
while True:
    # Enter the initial value in the input box
    try:
        start_index_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "tableForm:startIndex"))
        )
        start_index_box.clear()
        start_index_box.send_keys(str(start_value))
    except Exception as e:
        print("Error entering the initial value:", e)
        continue  # Retry on the next loop iteration
    
    # Click the Select button
    try:
        select_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "tableForm:selectButton"))
        )
        select_button.click()
    except Exception as e:
        print("Error clicking the Select button:", e)
        continue  # Retry on the next loop iteration

    # Wait briefly to ensure files are selected before proceeding to download
    time.sleep(2)
    
    # Click the "DOWNLOAD SELECTED as zip" button
    try:
        download_zip_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'DOWNLOAD SELECTED as zip')]"))
        )
        download_zip_button.click()
    except Exception as e:
        print("Error clicking the Download Selected as zip button:", e)
        continue  # Retry on the next loop iteration

    print(f"Downloaded batch starting from index {start_value}.")

    # Increment the start value for the next batch
    start_value += 500

    # Wait briefly before moving to the next batch to avoid any overlap
    time.sleep(2)
