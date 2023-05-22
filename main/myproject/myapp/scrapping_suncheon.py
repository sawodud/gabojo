import requests
from bs4 import BeautifulSoup
import os
import sys
from selenium import webdriver # webdriver를 이용해 해당 브라우저를 열기 위해
from pyvirtualdisplay import Display
from selenium.webdriver.common.keys import Keys # 키보드 입력을 할 수 있게 하기 위해
from selenium.webdriver.common.by import By # html요소 탐색을 할 수 있게 하기 위해
from selenium.webdriver.chrome.service import Service
import time

def create_soup(url):
    res = requests.get(url) # html 문서 가져오기 위한 요청
    res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동
    soup = BeautifulSoup(res.text, "lxml") # res.text를 통해 가져온 HTML 문서를 lxml 파서를 통해서 BeautifulSoup 객체로 만들어 줌
    return soup

def scrape_image_link(link, image_link): # 이미지 크롤링
    url = link
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    try:
        new_image_link = soup.find("div", attrs={"class" : "ssrcss-ab5fd8-StyledFigureContainer e34k3c21"}).find("img")["src"]
        image_link.append(new_image_link)
    except:
        try:
            display = Display(visible=0, size=(1920, 1080))
            display.start()
            path = '/home/ubuntu/chromedriver'
            s=Service(path)
            driver = webdriver.Chrome(service=s)
            driver.get(url)
            driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="smphtml5iframebbcMediaPlayer0"]'))
            image = driver.find_element(By.XPATH, '//*[@id="mediaContainer"]/img').get_attribute('src')
            driver.switch_to.default_content()
            image_link.append(image)
            driver.quit()
            display.stop()
        except:
            image_link.append('https://search.pstatic.net/sunny/?src=https%3A%2F%2Fimage.utoimage.com%2Fpreview%2Fcp952602%2F2021%2F05%2F202105018297_500.jpg&type=sc960_832')


def scrape_suncheon(): # 여행지 크롤링
    url = "https://trip.place.naver.com/list?query=%EC%88%9C%EC%B2%9C%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&level=top&zoomLevel=10.000"
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    suncheon_list = soup.find("ol", attrs={"class" : "gel-layout__item gs-u-float-left@l"}).find_all("li")

    arr=[]
    image_link=[]
    name=[]
    for tour in enumerate(suncheon_list):
        title = tour.find("a").get_text().strip() # strip 앞뒤 공백제거 get_text 하위태그 제거하고 유니코드 텍스드문자열 반환
        link = url.replace('/https://trip.place.naver.com/list?query=%EC%88%9C%EC%B2%9C%20%EA%B0%80%EB%B3%BC%EB%A7%8C%ED%95%9C%EA%B3%B3&level=top&zoomLevel=10.000', '')+tour.find("a")["href"]
        #scrape_image_link(link, image_link)
        scrape_content(link, name)
        arr.append(title + '\n' + link + '\n')

    if os.path.exists('suncheon.txt'):
        os.remove('suncheon.txt')
    

    suncheon_fp = open('suncheon.txt','w',encoding='utf-8')
    for i in range(len(arr)):
        bbc_fp.writelines(arr[i])

    for i in range(len(image_link)):
        bbc_fp.writelines(image_link[i] + '\n')
    
    suncheon_fp.close()

if __name__ == "__main__":
    scrape_news()
    
    '''