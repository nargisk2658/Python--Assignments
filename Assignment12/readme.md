# Selenium Automation Project - Google Search

## 📌 Description
This project demonstrates browser automation using Selenium WebDriver in Python.  
It performs a Google search, extracts results, interacts with elements, and demonstrates navigation.

---

## 📁 Project Structure

Assignment12/
 ├── automation.py
 ├── README.md

---

## 🚀 Features Implemented

### ✅ Browser Automation
- Opens Chrome browser  
- Navigates to Google  

### ✅ Search Functionality
- Uses `By.NAME` to locate search box  
- Enters query and submits  

### ✅ Data Extraction
- Extracts top 5 search results  
- Uses `By.CSS_SELECTOR`  

### ✅ Element Interaction
- Clicks first result using `By.XPATH`  

### ✅ Navigation Methods
- `driver.back()`  
- `driver.forward()`  
- `driver.refresh()`  

### ✅ Locator Strategies Used
- `By.ID`  
- `By.NAME`  
- `By.XPATH`  
- `By.CSS_SELECTOR`  

### ✅ Explicit Waits
- Uses `WebDriverWait` instead of `time.sleep()`  

### ✅ Validation Handling
- Checks if results exist  
- Handles exceptions safely  

---

## 🛠️ Requirements

- Python 3.x  
- Google Chrome  
- ChromeDriver (matching version)

---

## 📦 Installation Steps

1. Install Selenium:
pip install selenium

2. Download ChromeDriver:
https://chromedriver.chromium.org/downloads

3. Add ChromeDriver to system PATH  

---

## ▶️ How to Run

python automation.py

---

## 📊 Output

- Displays top 5 Google search results  
- Opens first result  
- Demonstrates browser navigation  

---

## 📌 Notes

- This project is built for learning Selenium basics  
- Uses best practices like explicit waits and multiple locator strategies  
- README accurately reflects implemented functionality  
