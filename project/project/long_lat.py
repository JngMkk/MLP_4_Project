import pandas as pd
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
import pyautogui
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='app_name')

# 위도, 경도 반환하는 함수
def geocoding(address):
    geo = geolocator.geocode(address)
    crd = [geo.latitude, geo.longitude]
    print(crd)

raw_univ = '서울기독대 예원예술대 경주대 금강대 대구예술대 신경대 제주국제대 한국국제대 한려대 두원공대 부산과학기술대 서라벌대 강원관광대 고구려대 광양보건대 대덕대 영남외대 웅지세무대'
raw_univ = raw_univ.split()
# print(raw_univ)






service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
# actionChains = ActionChains(driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')

univ_name_list = []
address_list = []
latitude_list = []
longitude_list = []

def find_address(univ_name):
    url = 'https://www.google.com/maps/'
    driver.implicitly_wait(3)
    driver.get(url)
    driver.maximize_window()
    searchbox = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    searchbox.send_keys(univ_name)
    search = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    search.click()
    sleep(2)
    address = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
    pyautogui.moveTo(1166, 548)
    pyautogui.click(button='right')
    loc = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/ul/li[1]/div[3]/div[1]')
    print(type(loc.text), loc.text)
    address_text = address.text
    sleep(3)

    univ_name_list.append(univ_name)
    address_list.append(address_text)
    latitude_list.append(loc.text.split(',')[0])
    longitude_list.append(loc.text.split(',')[1])

    # print(pyautogui.position()) #1166, 548 / 1920, 1080
    # print(pyautogui.size())


'''
    # lat_long_url = 'https://www.latlong.net/convert-address-to-lat-long.html'
    # driver.get(lat_long_url)
    # driver.implicitly_wait(3)
    # searchbox2 = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/form/input')
    # sleep(6)
    # searchbox2.send_keys(address_text)
    # find_btn = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/form/button')
    # find_btn.click()
    # driver.implicitly_wait(5)
    # lat = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[1]/div[1]/input')
    # long = driver.find_element(By.XPATH, '/html/body/main/div[2]/div[1]/div[1]/div[2]/input')
    # print('lat: ',lat.get_attribute('value'))
    # print('long: ',long.get_attribute('value'))
'''

for i in range(len(raw_univ)):
    find_address(raw_univ[i])

loc_address_data = {'name': univ_name_list,
                    'address': address_list,
                    'latitude': latitude_list,
                    'longitude': longitude_list}

loc_df1 = pd.DataFrame(loc_address_data)
loc_df1.to_csv('./data/location.csv')

