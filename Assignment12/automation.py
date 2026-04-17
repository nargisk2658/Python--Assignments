# automation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Chrome options (stable + no auto issues)
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # Open Google
    driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)

    # Find search box (NAME)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    
    # Enter query
    search_box.send_keys("Python Selenium tutorial")
    search_box.send_keys(Keys.RETURN)

    # Wait for results (CSS SELECTOR)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3")))

    # Get results
    results = driver.find_elements(By.CSS_SELECTOR, "h3")

    print("\nTop Google Search Results:\n")

    if results:
        for i, result in enumerate(results[:5], start=1):
            print(f"{i}. {result.text}")
    else:
        print("No results found.")

    # Click first result (XPATH)
    try:
        first = wait.until(EC.element_to_be_clickable((By.XPATH, "(//h3)[1]")))
        first.click()
    except:
        print("Could not click first result")

    # Navigation
    driver.back()
    driver.forward()
    driver.refresh()

    # ID locator example
    try:
        wait.until(EC.presence_of_element_located((By.ID, "logo")))
        print("Logo found using ID locator")
    except:
        print("Logo not found")

except Exception as e:
    print("Error occurred:", e)

# 🔥 IMPORTANT: prevents auto close
input("\nPress ENTER to close browser...")

driver.quit()