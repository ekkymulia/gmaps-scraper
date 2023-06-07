# Import the library Selenium
import time

from selenium import webdriver
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
    "https://www.google.com/maps/place/Apartemen+Tamansari+Sudirman/@-6.216428,106.8187557,796m/data=!3m2!1e3!4b1!4m6!3m5!1s0x2e69f4008bf925cb:0x9f7528e73e923bda!8m2!3d-6.2164333!4d106.8213306!16s%2Fg%2F1ptx_4qd3"

]

# Initialize variables and declare it 0
i = 0
data_list = []
set_check = []

# Create a loop for obtaining data from URLs
for i in range(len(url)):

    # Open the Google Map URL
    browser.get(url[i])

    time.sleep(5);

    title =browser.find_element(By.CLASS_NAME,
        "DUwDvf")
    address = browser.find_element(By.CLASS_NAME,
        "Io6YTe")

    print(title.text)
    print(address.text)

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