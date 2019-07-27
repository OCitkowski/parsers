import requests
from bs4 import BeautifulSoup
import csv
import timing
from time import sleep

from multiprocessing import Pool


def write_csv(data):
    # with open('names.csv', 'a') as file:
    #     writer = csv.writer(file, delimiter=',', dialect='excel')
    #     writer.writerow((data['address'], data['code'], data['last_checked']))

    with open('names.csv', 'a') as file:
        order = ['address', 'code', 'last_checked']
        writer = csv.DictWriter(file, fieldnames=order, delimiter=',', dialect='excel')
        writer.writerow(data)


def get_html(url, url_proxy=None):
    headers = {
        'User - Agent': 'Mozilla / 5.0(X11; Ubuntu; Linux x86_64; rv: 68.0) Gecko / 20100101 Firefox / 68.0',
        'Accept - Language': 'en - US, en; q = 0.5',
        'Accept - Encoding': 'gzip, deflate, br',
        'Connection': 'keep - alive'
    }

    if url_proxy:
        r = requests.get(url, headers=headers, proxies=url_proxy)

    else:
        r = requests.get(url, headers=headers)

    print('********')
    return r.text


def get_proxy(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='proxylisttable').find('tbody').find_all('tr')

    i = 0

    with open('names.csv', 'w') as file:
        file.truncate()
        file.close()

    for tr in trs:
        i += 1
        tds = tr.find_all('td')

        if 'yes' in tr.find('td', class_='hx').text.strip():
            schema = 'https'
        else:
            continue

        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        code = tds[2].text.strip()

        last_checked = tds[7].text.strip()

        proxy = {'address': schema + '://' + ip + ':' + port, 'code': code, 'last_checked': last_checked}

        write_csv(proxy)


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find_all('div', class_='content-wrap')

    return h1


# def make_all(url):
#     text = get_html(url)
#     get_data(text)

def main():
    # url = 'https://www.dcz.gov.ua/userSearch/vacancy?koatuuVal=101010510100000&koatuuLab=%D0%92%D1%96%D0%BD%D0%BD%D0%B8%D1%86%D1%8F&regionID=101010500000000&activePage=4&itemsPerPage=100'
    # print(get_data(get_html(url)))

    url_proxes_site = 'https://free-proxy-list.net'

    url_proxy = {
        'https': 'https://185.158.9.27:34290'
        # 'https': 'https://195.211.230.253:40896'
    }

    # get_proxy(get_html(url_proxes_site, url_proxy))
    # get_proxy(get_html(url_proxes_from_site))

    # with open('names.csv') as file:
    #     order = ['address', 'code', 'last_checked']
    #     reader = csv.DictReader(file, fieldnames=order)
    #     for row in reader:
    #         # print(row)
    #         print(row['address'])
    sleep(5)

    # with Pool(20) as p:
    #   p.map(make_all, urls)


if __name__ == '__main__':
    main()
