from flask import Blueprint, render_template, request
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


import time
import json


# 루트
bp = Blueprint("artist", __name__, url_prefix="/artist")


# /artist 경로에서
@bp.route("/", methods=["GET"])
def index():

    driver = webdriver.Chrome()  # 드라이버 설정

    driver.implicitly_wait(10)  # 10초안에 웹페이지 로드시 바로 넘어감

    artist_id_num = request.args.get("artist_id_num")

    # print(artist_id_num)

    default_url = "https://www.melon.com/artist/timeline.htm?artistId="

    url = default_url + artist_id_num 

    # print(url)

    driver.get(url)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "more")))

    html =  driver.page_source

    # print(html)

    soup = BeautifulSoup(html, "html.parser")  # SOUP 객체로 웹사이트 변환

    # print(soup)


    wrap_info = soup.select_one("div.dtl_atist")


    # wrap_info = soup.select_one("#wrap > #cont_wrap > #conts_section > #conts >  div.wrap_dtl_atist > div.dtl_atist clfix")

    # print(wrap_info)

    img_url = wrap_info.select_one("#artistImgArea > img")["src"]

    # print(img_url)

    artist_info = wrap_info.select_one("div.wrap_atist_info")

    # print(artist_info)

    artist_name = artist_info.select_one("p.title_atist").text

    artist_name = artist_name[5:]

    # print(artist_name)

    artist_group_names = artist_info.select("a.atistname > span")

    # print(artist_group_names[0])
    # print(artist_group_names[1])
    # print(artist_group_names[2])
    # print(artist_group_names[3])
    # print(artist_group_names[4])




    namelist = []

    for el in artist_group_names[::2]:
        el = str(el)
        name = el[6:-7]
        namelist.append(name)
        
    # print(namelist)

    artist_group_names = ', '.join(s for s in namelist)

    # print(artist_group_names)

    debut = artist_info.select_one("span.gubun").text

# print(debut)

    music = artist_info.select_one(
        "span.songname12"
    ).text

    # print(music)

    info_list = artist_info.select("dd")

    # print("dd")

    a_type = str(info_list[1])[4:-5]
    
    company = str(info_list[2])[4:-5]

    # print(company)
     
    fan_num = wrap_info.select_one("#d_like_count").text

    # print(fan_num)

    artists = {}

    artists["artist_name"] = artist_name
    artists["artist_group_names"] = artist_group_names
    artists["debut"] = debut
    artists["music"] = music
    artists["company"] = company
    artists["img_url"] = img_url
    artists["fan_num"] = fan_num

    print(artists)



    # print(artists)

    driver.quit()


    return render_template("artist.html", artist_info = artists)
