# Import the library Selenium
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import pandas

# Make browser open in background
options = webdriver.ChromeOptions()
options.add_argument('headless')

# Create the webdriver object
browser = webdriver.Chrome(
    "chromedriver_win32\chromedriver.exe"
)

# Obtain the Google Map URL
#restaurant "https://www.google.com/maps/search/Restaurants/@-6.179569,106.7892086,17z/data=!4m2!2m1!6e5"
#cafe "https://www.google.com/maps/search/caf%C3%A8/@-6.1783106,106.7894188,17z/data=!4m2!2m1!6e5
url = [
    "https://www.google.com/maps/place/Waroeng+ngupi-ngupi/@-6.2274602,106.8233662,256m/data=!3m1!1e3!4m10!1m2!2m1!1srestoran+di+bellagio+mall+kuningan!3m6!1s0x2e69f3e4ad1f5d53:0x3b893af478a8b9c5!8m2!3d-6.2275843!4d106.8243079!15sCiJyZXN0b3JhbiBkaSBiZWxsYWdpbyBtYWxsIGt1bmluZ2FuIgOIAQFaJCIicmVzdG9yYW4gZGkgYmVsbGFnaW8gbWFsbCBrdW5pbmdhbpIBE2phdmFuZXNlX3Jlc3RhdXJhbnSaASNDaFpEU1VoTk1HOW5TMFZKUTBGblNVUm5lVzh6TlVkM0VBReABAA!16s%2Fg%2F1yg4d0wb1 "
    # "https://www.google.com/maps/search/universitas/@-6.1985962,106.8440827,14.75z"
]


# Initialize variables and declare it 0
i = 0
data_list = []
set_check = []

# Create a loop for obtaining data from URLs
for i in range(len(url)):

    # Open the Google Map URL
    browser.get(url[i])

    time.sleep(10)

    # browser.find_element(By.ID, "searchboxinput").send_keys("Apartemen Kalibata city", Keys.ENTER)
    # time.sleep(5)
    # title =browser.find_element(By.CLASS_NAME,
    #     "DUwDvf")
    # address = browser.find_element(By.CLASS_NAME,
    #     "Io6YTe")
    #
    # print(title.text)
    # print(address.text)

    # Obtain the title of that place
    card = browser.find_elements(By.CLASS_NAME,
        "UaQhfb")

    for t in card:
        title = t.find_element(By.CLASS_NAME, "qBF1Pd").text
        if title not in set_check:
            try:
                rate_score = t.find_element(By.CLASS_NAME, "MW4etd").text
            except:
                rate_score = 0

            try:
                rate_many = int(t.find_element(By.CLASS_NAME, "UY7F9").text.strip("(").strip(")").replace('.', ''))
            except:
                rate_many = 0

            data_list.append({
                "title": title,
                "rate_score": rate_score,
                "rate_many": rate_many
            })

            set_check.append(title)
        else:
            continue

    for each in sorted(data_list, key=lambda d: d['rate_many'], reverse=True):
        print(f"{each['title']} - {each['rate_score']} - {each['rate_many']} review")


    # for each in data_list:
    #     print(f"{each['title']} - {each['rate_score']} - {each['rate_many']} review")

    # title = browser.find_elements(By.CLASS_NAME,
    #     "qBF1Pd")
    # rate_score = browser.find_elements(By.CLASS_NAME,
    #     "MW4etd")
    # rate_many = browser.find_elements(By.CLASS_NAME,
    #     "UY7F9")


    # for t in range(len(title)):
    #     data_list.append({
    #         "title": title[t].text,
    #         "rate_score": rate_score[t].text,
    #         "rate_many": int(rate_many[t].text.strip("(").strip(")").replace('.', ''))
    #     })
    #
    # sorted(data_list.iterkeys(), key=lambda k: data_list["rate_many"], reverse=True)

    # # Obtain the ratings of that place
    # stars = browser.find_element(By.CLASS_NAME, "aMPvhf-fI6EEc-KVuj8d")
    # print("The stars of restaurant are:", stars.text)
    #
    # # Obtain the description of that place
    # description = browser.find_element(By.CLASS_NAME,"uxOu9-sTGRBb-T3yXSc")
    # print("Description: ", description.text)
    #
    # # Obtain the address of that place
    # address = browser.find_elements(By.CLASS_NAME,"CsEnBe")[0]
    # print("Address: ", address.text)
    #
    # # Obtain the contact number of that place
    # phone = browser.find_elements(By.CLASS_NAME,"CsEnBe")[-2]
    # print("Contact Number: ", phone.text)
    #
    # # Obtain the reviews of that place
    # review = browser.find_elements(By.CLASS_NAME,"OXD3gb")
    # print("------------------------ Reviews --------------------")
    # for j in review:
    #     print(j.text)
    # print("\n")