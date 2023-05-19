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

def scrape_suncheon():
    url = "https://www.tripadvisor.co.kr/Attraction_Review-g1074108-d6847906-Reviews-Yeosu_Ocean_Rail_Bike-Yeosu_Jeollanam_do.html"
    res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    soup = create_soup(url)
    news_list = soup.find("div", attrs={"class" : "ui_columns is-multiline is-mobile"})
    arr=[] # title 하고 link 정보  attrs : 속성값 모두 출력
    image_link=[] 
    article=[]
    print(news_list)

    '''
    for news in enumerate(news_list):
        title = news.find("a").get_text().strip() # strip 앞뒤 공백제거 get_text 하위태그 제거하고 유니코드 텍스드문자열 반환
        link = url.replace('/news', '')+news.find("a")["href"]
        #scrape_image_link(link, image_link)
        scrape_content(link, article)
        arr.append(title + '\n' + link + '\n')
    '''
    '''
    arr=[] # title 하고 link 정보  attrs : 속성값 모두 출력
    image_link=[] 
    article=[]
    for news in enumerate(news_list):
        title = news.find("a").get_text().strip() # strip 앞뒤 공백제거 get_text 하위태그 제거하고 유니코드 텍스드문자열 반환
        link = url.replace('/news', '')+news.find("a")["href"]
        scrape_image_link(link, image_link)
        scrape_content(link, article)
        arr.append(title + '\n' + link + '\n')
    '''

if __name__ == "__main__":
    scrape_suncheon()