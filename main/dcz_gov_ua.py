import requests
from bs4 import BeautifulSoup
import csv
import timing
from time import sleep
from multiprocessing import Pool
import fake_useragent
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_html(url, url_proxy=None):
    # header = {
    #     'User - Agent': 'Mozilla / 5.0(X11; Ubuntu; Linux x86_64; rv: 68.0) Gecko / 20100101 Firefox / 68.0',
    #     'Accept - Language': 'en - US, en; q = 0.5',
    #     'Accept - Encoding': 'gzip, deflate, br',
    #     'Connection': 'keep - alive'
    # }
    # Random User-Agent

    # header = {
    #     'Host': 'www.dcz.gov.ua',
    #     'User - Agent': 'Mozilla / 5.0(X11; Ubuntu; Linux x86_64; rv: 68.0) Gecko / 20100101 Firefox / 68.0',
    #     'Accept': '* / *',
    #     'Accept - Language': 'en - US, en; q = 0.5',
    #     'Accept - Encoding': 'gzip, deflate, br',
    #     'Referer': 'https: // www.dcz.gov.ua / userSearch / vacancy?koatuuVal = 101010510100000 & koatuuLab = % D0 % 92 % D1 % 96 % D0 % BD % D0 % BD % D0 % B8 % D1 % 86 % D1 % 8 F & regionID = 101010500000000 & activePage = 2 & itemsPerPage = 15',
    #     'Content - Type': 'application / json; charset = UTF - 8',
    #     'Origin': 'https: // www.dcz.gov.ua',
    #     'Content - Length': '97',
    #     'Connection': 'keep - alive',
    #     'Cookie': 'UserPreference_OfficeSuite = MS; has_js = 1'
    # }

    ua = fake_useragent.UserAgent()
    user = ua.random
    header = {'User-Agent': str(user)}

    params = {"StartRowIndex": 15, "MaximumRows": "15", "RegionID": "101010500000000", "KoatuuID": "101010510100000"}

    r = requests.post(url, params=params, headers=header)

    print(r.text)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('div', class_='el-row shadow-resume-card')

    return h1


def main():
    driver = webdriver.Firefox()
    driver.get(
        "https://www.dcz.gov.ua/userSearch/vacancy?koatuuVal=101010510100000&koatuuLab=%D0%92%D1%96%D0%BD%D0%BD%D0%B8%D1%86%D1%8F&regionID=101010500000000&activePage=1&itemsPerPage=15")

    sleep(10)
    elements = driver.page_source
    # find_elements_by_class_name('el-row shadow-resume-card')
    # elements = driver.find_elements_by_xpath('el-row shadow-resume-card')

    print(elements)
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    driver.close()


if __name__ == '__main__':
    main()
