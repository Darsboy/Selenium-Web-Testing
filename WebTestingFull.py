from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://www.zolo.ca/'
city = 'Newmarket'
nei = 'Stonehaven-Wyndham'

def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

def get_Neighbourhoods():
    d = webdriver.Firefox()
    #d.implicitly_wait(3)
    d.get(url)
    #d.implicitly_wait(15)
    d.maximize_window()
    e = get_ele_times(d, 10 , lambda d: d.find_element_by_xpath('//*[@id="sarea"]'))
    e.clear()
    e.send_keys(city)
    es = d.find_element_by_xpath('/html/body/div[1]/header/nav/div[1]/div[2]/form/div/button/i')
    es.click()
    d.implicitly_wait(20)
    d.find_element_by_xpath('/html/body/div[1]/main/section[1]/ul/li[4]/a').click()
    #d.find_element_by_link_text('Neighbourhoods').click()
    d.implicitly_wait(20)
    #neisw = d.find_element_by_xpath('/html/body/div[1]/section[2]/div/section/table/tbody/tr[6]/td[1]/a')
    #neisw.click()
    d.find_element_by_link_text(nei).click()
    d.get_screenshot_as_file('neisw.png')
    d.close()
get_Neighbourhoods()