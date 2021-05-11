import csv
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/Downloading/SystemDesign2/chromedriver_win32/chromedriver')
driver.get("https://downtowndallas.com/experience/stay/")

#list of links of hotels,
linkofhotels = []

maincontent = driver.page_source
soupmain = BeautifulSoup(maincontent)

for hotels in soupmain.find_all(attrs='place-square__btn'):
    link = hotels.get('href')
    if link not in linkofhotels:
        linkofhotels.append(link)
driver.close()
with open("link.csv", "a") as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(linkofhotels)

for link in linkofhotels:
    results = []
    driver = webdriver.Chrome(executable_path='D:/Downloading/SystemDesign2/chromedriver_win32/chromedriver')
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    name = soup.h1.string
    if name not in results:
        results.append(name)
    for element in soup.find_all(attrs='place-info-address'):
        link = element.a
        t = link.get_text("|", strip=True)
        if t not in results:
            results.append(t)
    image = soup.find(attrs='place-info-image')
    img = image.img
    imglink = img.get("src")
    if imglink not in results:
        results.append(imglink)
    with open("output.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(results)
    driver.close()






