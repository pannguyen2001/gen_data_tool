from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from io import StringIO
import pandas as pd

# Step 1: Setup WebDriver
# Set up the web driver
chrome_options = webdriver.ChromeOptions()
# Uncomment the line below to run Chrome in headless mode (not show UI)
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) # , options=chrome_options add here if you want to run Chrome in headless mode

# Step 2: Open the webpage in a browser
url = "https://www.worldometers.info/world-population/population-by-country/"
# "https://en.wikipedia.org/wiki/Provinces_of_Vietnam"
# 'https://www.pro-football-reference.com/teams/dal/2024_roster.htm'
driver.get(url)
driver.maximize_window() # Optional: maximize the window

# Wait for all tables to load
wait_time = 30
wait = WebDriverWait(driver, wait_time)

# Wait until all tables with class "wikitable" are present
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "table"))) # Find by class name/tagname,x_path,..., return True if all elements are present, otherwise raise TimeoutException
# Can use wait.until as a condition before get element ?
# Find all tables with class "wikitable"
tables = driver.find_elements(By.TAG_NAME, "table")
"""
    return list of <selenium.webdriver.remote.webelement.WebElement> objects
    example: [
    <selenium.webdriver.remote.webelement.WebElement (session="de02b5ca65b716d365f2eabcbfbc3d94", element="f.DB82BC546E546F512C6474FE81D47516.d.D87BB138261B34642EB8FBD96E39220A.e.95")>,
    <selenium.webdriver.remote.webelement.WebElement (session="de02b5ca65b716d365f2eabcbfbc3d94", element="f.DB82BC546E546F512C6474FE81D47516.d.D87BB138261B34642EB8FBD96E39220A.e.96")>
    ]
"""

# Step 3: Extract data from tables
# Parse all tables into DataFrames
dataframes = []
for index, table in enumerate(tables):
    # Get the HTML content of the table, include the tags: table, tr, td,..
    # other properties: element.text: get text only, element.get_attribute('outerHTML'): get all properties, element.get_attribute('innerHTML'): get all properties except tags
    html = table.get_attribute('outerHTML')
    try:
        # Parse the HTML content into a DataFrame
        df = pd.read_html(StringIO(html))[0]
        # Add the DataFrame to the list
        dataframes.append(df)
        # Save the DataFrame to a CSV file
        df.index = df.index + 1
        df.to_csv(f"population-by-country.csv")
        print(f"\n✅ Table {index + 1}:\n", df)
    except ValueError as e:
        print(f"⚠️ Skipping table {index + 1}: {e}")

driver.save_screenshot('screenshot.png')

# Step 4: Clean up
driver.quit()

