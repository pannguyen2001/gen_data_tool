
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 30)

# my_url= "https://helplandingpage.misa.vn/knowledge-base/danh-sach-ten-mien-pho-bien/"
# driver.get(my_url)
# #actions = ActionChains(driver)

# table = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.TAG_NAME, "table")))
# trs = table.find_elements(By.TAG_NAME, "tr")
# print(len(trs))
# countries = []
# for tr in trs:
#     tds = tr.find_elements(By.TAG_NAME, "td")
#     for td in tds:
#         print(td.get_attribute('innerText'))

# # =========== Get data from table using pandas.read_html ============
# Crawl email domain by using pandas.read_html
# import pandas as pd
# from src.helpers import write_data_to_csv_file
# from src.craw_data import get_table_data_from_html

# url='https://helplandingpage.misa.vn/knowledge-base/danh-sach-ten-mien-pho-bien/'

# url1 = "https://diendantuyensinh24h.com/danh-sach-cac-truong-dai-hoc-va-hoc-vien-toan-quoc/"

# df = get_table_data_from_html(url1)
# print(df[0].to_dict("records"))
# # df = df[0]
# # df.loc[0,:] = ["Order", "Email_suffix"]
# # df.columns = df.loc[0,:]
# # email_suffix_data_list = df.to_dict("list").get("Email_suffix")
# # print(email_suffix_data_list)

# # write_data_to_csv_file(email_suffix_data_list, "./src/data/email_suffix.csv")

# # =========== Get data from table using pandas.read_html ============

# # =========== Get data from table using selenium ============
# Crawl university by using selenium

# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from src import logger
# from src.helpers import write_data_to_csv_file

# # Initialize the Chrome driver
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()
# # wait up to 50 seconds
# wait = WebDriverWait(driver, 50)

# # Open the webpage with the table
# driver.get("https://thi.tuyensinh247.com/danh-sach-truong-dai-hoc-tai-viet-nam-phan-chia-theo-vung-mien-c24a80591.html")

# # Wait for the table body rows to be visible
# table = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "table")))

# # Find all rows in the table
# rows = table.find_elements(By.TAG_NAME, "tr")

# # Prepare a DataFrame to store the data
# df_university = pd.DataFrame(columns=["Code","Name"])

# # Iterate over each row and extract cell data
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     row_data = [cell.text for cell in cells]
#     if len(row_data) == 4 and row_data[0].isdigit():
#         df_university.loc[len(df_university)] = row_data[1:-1]
#         logger.info(row_data)

# driver.quit()

# # Process data
# # Remove unwanted characters
# remove_chars = "()*"
# translation_table = str.maketrans('', '', remove_chars)
# df_university["Name"] = df_university["Name"].str.title().str.translate(translation_table).str.strip()
# df_university["Code"] = df_university["Code"].str.strip()

# # Sort data by ascending code
# df_university = df_university.sort_values(by="Code", ascending=True)

# # Remove duplicate rows based on "Code" and "Name" columns
# df_university = df_university.drop_duplicates(subset=["Code", "Name"], keep="first")

# # # Reset index
# # df_university = df_university.reset_index(drop=True)
# # df_university.index = df_university.index + 1  # Make index start from 1
# # df_university = df_university.reset_index()

# # Combine code and name
# df_university["University"] = "(" + df_university["Code"] + ") " + df_university["Name"]

# # Drop unnecessary columns
# df_university = df_university.drop(columns=["Code", "Name"])

# logger.info(df_university)

# # Write data to CSV file
# write_data_to_csv_file(df_university, "./src/data/university_name_and_code.csv")

# =========== Get VN province, ward data ============
import pandas as pd
from requests import get
from src import logger
from src.helpers import write_data_to_csv_file

# config = {
#     "province":{
#         "url": "https://provinces.open-api.vn/api/p?depth==2",
#         "file_name": "./src/data/province_2024.csv"
#     },
#     "district":{
#         "url": "https://provinces.open-api.vn/api/d?depth=2",
#         "file_name": "./src/data/district_2024.csv"
#     },
#     "ward":{
#         "url": "https://provinces.open-api.vn/api/w?depth=2",
#         "file_name": "./src/data/ward_2024.csv"
#     }
# }

# for data_config in config.values():
#     response = get(data_config.get("url"))
#     data = response.json()
#     df = pd.DataFrame(data)
#     write_data_to_csv_file(df, data_config.get("file_name"))
#     logger.info(df)


# =========== Process VN province, district, ward data to 1 file only ============
# df_province = pd.read_csv("./src/data/province_2024.csv")
# df_province = df_province[["code", "name"]]
# df_province = df_province.rename(columns={"name": "province", "code": "province_code"})

# df_district = pd.read_csv("./src/data/district_2024.csv")
# df_district = df_district[["code", "name", "province_code"]]
# df_district = df_district.rename(columns={"name": "district", "code": "district_code", "province_code": "province_code"})

# df_district = df_district.merge(df_province, on="province_code", how="left")

# df_ward = pd.read_csv("./src/data/ward_2024.csv")
# df_ward = df_ward[["code", "name", "district_code"]]
# df_ward = df_ward.rename(columns={"name": "ward", "code": "ward_code", "district_code": "district_code"})

# df_ward = df_ward.merge(df_district, on="district_code", how="left")
# df_ward = df_ward.drop_duplicates()
# df_ward = df_ward.drop(columns=["ward_code", "district_code", "province_code"])

# df_ward = df_ward.sort_values(by=["province", "district", "ward"], ascending=True)
# logger.info(df_ward)
# write_data_to_csv_file(df_ward, "./src/data/vn_address_2024.csv")
