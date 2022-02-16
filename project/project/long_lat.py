from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='app_name')

# 위도, 경도 반환하는 함수
def geocoding(address):
    geo = geolocator.geocode(address)
    crd = [geo.latitude, geo.longitude]
    print(crd)

raw_univ = '서울기독대 예원예술대 경주대 금강대 대구예술대 신경대 제주국제대 한국국제대 한려대 두원공대 부산과학기술대 서라벌대 가원관광대 고구려대 광양보건대 대덕대 영남외대 웅지세무대'
raw_univ = raw_univ.split()
print(raw_univ)




service = webdriver.chrome.service.Service('../drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
# actionChains = ActionChains(driver)

soup = BeautifulSoup(driver.page_source, 'html.parser')

def find_loc(univ_name):
    url = 'https://www.google.com/maps/'
    driver.implicitly_wait(3)
    driver.get(url)
    # driver.maximize_window()
    searchbox = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
    searchbox.send_keys(univ_name)
    search = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    search.click()
    sleep(2)
    # loc = driver.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/ul/li[1]')
    # loc.click
    address = driver.find_element(By.XPATH, '/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]')
    # red_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]')
    # achains = ActionChains(driver)
    # achains.move_to_element(red_button).perform()
    # sleep(2)
    # achains.context_click('/html/body/div[3]/div[3]/div[1]').perform()
    # loc = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[1]/ul/li[1]/div[3]/div[1]')
    address_text = address.text
    with open('address.txt', 'a', encoding='utf-8') as f:
        f.write(f"{univ_name}: {address_text},\n")
        # geocoding(address_text)
    sleep(3)


    # lat_long_url = 'https://www.latlong.net/convert-address-to-lat-long.html'
    # driver.implicitly_wait(2)
    # driver.get(lat_long_url)
    # searchbox2 = driver.find_element(By.XPATH, '//*[@id="vi3338"]')
    # sleep(2)
    # searchbox2.send_keys(address_text)
    # find_btn = driver.find.element(By.XPATH, '//*[@id="btnfind"]')
    # find_btn.click()



for i in range(len(raw_univ)):
    find_loc(raw_univ[i])








