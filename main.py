from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
import csv
import time


url = "https://www.carbravo.com/shopping/inventory/search?amountFinanced=58130.66&apr=10.34&comparedVins=&dealerPrice=54557&downPayment=2000&financeTerms=72&paymentType=CASH&radius=500&sellingPrice=54557&sort=RELEVANCE%2CASC&zipCode=48243"  # Replace with your target URL



options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)



driver.implicitly_wait(3)


a_elements = driver.find_elements(by=By.TAG_NAME , value="a" )


filtered_hrefs = []

csv_file_path = "filtered_hrefs.csv"

for i in range(1, 30000, 800):
    driver.execute_script("window.scrollTo(0, {});".format(i))
    a_elements = driver.find_elements(by=By.TAG_NAME , value="a" )
    print('len elements :' , len(a_elements))
    for a_element in a_elements:
        link_href = a_element.get_attribute("href")
        if link_href and link_href.startswith("https://www.carbravo.com/shopping/inventory/vehicle?"):
            filtered_hrefs.append(link_href)
            filtered_hrefs = set(filtered_hrefs)
            filtered_hrefs = list(filtered_hrefs)
    print('lets sleep')
    time.sleep(3)
    with open(csv_file_path, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([filtered_hrefs])
        print('saved')
    print('len filtered' , len(filtered_hrefs))


driver.quit()


print(f"Filtered hrefs saved to {csv_file_path}")