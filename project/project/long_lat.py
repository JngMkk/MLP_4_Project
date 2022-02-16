from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='South Korea')

# 위도, 경도 반환하는 함수
def geocoding(address):
    location = geolocator.geocode(address)
    # x_y = [geo.latitude, geo.longitude]
    return type(location)

raw_univ = '서울기독대 예원예술대 경주대 금강대 대구예술대 신경대 제주국제대 한국국제대 한려대 두원공대 부산과학기술대 서라벌대 가원관광대 고구려대 광양보건대 대덕대 영남외대 웅지세무대'
raw_univ = raw_univ.split()
print(raw_univ)


url = 'https://www.google.com/maps/'

service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
actionChains = ActionChains(driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')

def find_loc(univ_name):
    driver.implicitly_wait(3)
    driver.get(url)
    driver.maximize_window()
    searchbox = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    searchbox.send_keys(univ_name)
    search = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    search.click()
    sleep(2)
    # loc = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/ul/li[1]')
    # loc.click
    ActionChains(driver)
    loc = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
    red_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]')
    # actionChains.context_click('/html/body/div[3]/div[3]/div[1]').perform()
    print(loc.text)




find_loc(raw_univ[1])








