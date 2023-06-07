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
    "C:\Software\chromedriver_win32\chromedriver.exe"
)

# Obtain the Google Map URL
#restaurant "https://www.google.com/maps/search/Restaurants/@-6.179769,106.7892086,17z/data=!4m2!2m1!6e7"
#cafe "https://www.google.com/maps/search/caf%C3%A8/@-6.1783106,106.7894188,17z/data=!4m2!2m1!6e7
url = [
    "https://www.google.com/maps/@-6.492794,106.8314003,15z"

]

# Initialize variables and declare it 0
i = 0

data_list = []
set_check = set()
# card scraper
def card_scraper():
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

            set_check.add(title)
        else:
            continue

    i=0
    for each in sorted(data_list, key=lambda d: d['rate_many'], reverse=True):
        i+=1
        if i == 4:
            break

        print(f"{each['title']} - {each['rate_score']} - {each['rate_many']} review")



# Create a loop for obtaining data from URLs
keyword="Green Lake Sunter"
for i in range(len(url)):

    # Open the Google Map URL
    browser.get(url[i])

    time.sleep(7)

    browser.find_element(By.ID, "searchboxinput").send_keys(f"{keyword}", Keys.ENTER)

    time.sleep(4)
    try:
        browser.find_element(By.CLASS_NAME, "hfpxzc").click()

        time.sleep(4);

        title =browser.find_element(By.CLASS_NAME,
            "DUwDvf")
        address = browser.find_element(By.CLASS_NAME,
            "DkEaL")
    except:
        title =browser.find_element(By.CLASS_NAME,
            "DUwDvf")
        address = browser.find_element(By.CLASS_NAME,
            "DkEaL")

    print(title.text)
    print(address.text)
    print("=========")

    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("mall")
    try:
        browser.find_element(By.ID, "searchboxinput").send_keys(f"mall sekitar {keyword}", Keys.ENTER)
    except:
        print("mall -err ")
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
        "UaQhfb")
    data_list = []
    card_scraper()
    mall_list = sorted(data_list, key=lambda d: d['rate_many'], reverse=True)
    # mall_list = [
    #     {"title": "Cibubur Junction"}, {"title": "Transmart Cibubur"}, {"title": "Mall Ciputra Cibubur"}
    # ]
    print("=========")
    print("restoran")
    i=0
    for mall in mall_list:
        i+=1
        if i == 4:
            break

        time.sleep(5)
        browser.find_element(By.ID, "searchboxinput").clear()
        time.sleep(7)
        browser.find_element(By.ID, "searchboxinput").send_keys(f"restoran di {mall['title']}", Keys.ENTER)
        time.sleep(7)
        liElement = browser.find_element(By.XPATH, "//div[@role='feed']")
        browser.execute_script("window.scrollBy(0, 700)", liElement)
        time.sleep(7)
        # Obtain the card of that place
        card = browser.find_elements(By.CLASS_NAME,
                                     "UaQhfb")
        data_list = []
        print(mall)
        card_scraper()
        print("=========")


    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("starbucks")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"starbucks sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    try:
        # Obtain the card of that place
        card = browser.find_elements(By.CLASS_NAME,
                                     "UaQhfb")
        data_list = []
        card_scraper()
    except:
        title = browser.find_element(By.CLASS_NAME,
                                     "DUwDvf")
        print(title.text)
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("mcdonalds")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"mcdonalds sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    try:
        # Obtain the card of that place
        card = browser.find_elements(By.CLASS_NAME,
                                     "UaQhfb")
        data_list = []
        card_scraper()
    except:
        title = browser.find_element(By.CLASS_NAME,
                                     "DUwDvf")
        print(title.text)
    print("=========")

    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("supermarket")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"supermarket sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
        "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("pasar")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"pasar sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
        "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("ace")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"ace sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    try:
        # Obtain the card of that place
        card = browser.find_elements(By.CLASS_NAME,
                                     "UaQhfb")
        data_list = []
        card_scraper()
    except:
        title = browser.find_element(By.CLASS_NAME,
                                     "DUwDvf")
        print(title.text)
    print("=========")

    # copy sini
    # time.sleep(5)
    # browser.find_element(By.ID, "searchboxinput").clear()
    # time.sleep(5)
    # print("electro city")
    # browser.find_element(By.ID, "searchboxinput").send_keys(f"electronic city sekitar {keyword}", Keys.ENTER)
    # time.sleep(7)
    # try:
    #     # Obtain the card of that place
    #     card = browser.find_elements(By.CLASS_NAME,
    #                                  "UaQhfb")
    #     data_list = []
    #     card_scraper()
    # except:
    #     title = browser.find_element(By.CLASS_NAME,
    #                                  "DUwDvf")
    #     print(title.text)
    # print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("bioskop")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"bioskop sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    try:
        # Obtain the card of that place
        card = browser.find_elements(By.CLASS_NAME,
                                     "UaQhfb")
        data_list = []
        card_scraper()
    except:
        title = browser.find_element(By.CLASS_NAME,
                                     "DUwDvf")
        print(title.text)
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("rumah sakit")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"rumah sakit sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
                                 "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("guardian")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"guardian sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
                                 "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("century")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"century sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
                                 "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("cowork")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"co-working space sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
                                 "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("universitas")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"universitas sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
                                 "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")

    # copy sini
    time.sleep(5)
    browser.find_element(By.ID, "searchboxinput").clear()
    time.sleep(5)
    print("sekolah")
    browser.find_element(By.ID, "searchboxinput").send_keys(f"sekolah swasta sekitar {keyword}", Keys.ENTER)
    time.sleep(7)
    # Obtain the card of that place
    card = browser.find_elements(By.CLASS_NAME,
                                 "UaQhfb")
    data_list = []
    card_scraper()
    print("=========")



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