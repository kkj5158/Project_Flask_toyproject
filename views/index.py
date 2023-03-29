from flask import Blueprint, render_template, jsonify, request
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import time
import json


bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/ranking", methods=["GET"])
def index():
    # mac일경우

    # driver = webdriver.Chrome('/Users/dlruawo07/Downloads/chromedriver_mac_arm64/chromedriver')

    # window일경우

    driver = webdriver.Chrome()  # 드라이버 설정

    driver.implicitly_wait(10)  # 10초안에 웹페이지 로드시 바로 넘어감

    driver.get("https://www.melon.com/artistplus/artistchart/index.htm")

    while True:
        try:
            more = driver.find_element(
                By.XPATH, '//*[@id="conts"]/div[3]/div[3]/button/span/span'
            )
            more.click()
            driver.implicitly_wait(0.3)  # 0.3초안에 웹페이지 로드시 바로 넘어감
        except:
            break

    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")

    artists = []

    lists = soup.select(
        "#conts > div.ltcont > div.wrap_list_artistplus.d_artist_list > ul > li"
    )

    for el in lists:
        image_url = el.select_one("div.artistplus > div.wrap_thumb > a > img")["src"]
        rank = el.select_one("div.artistplus_li_wrap > span.rank").text
        wrap_info = el.select_one("div.artistplus > div.wrap_info > dl")
        name = wrap_info.select_one("dt > a").text
        fan = wrap_info.select_one("dd.gubun").text[2:10].strip()
        # 고유 아티스트 넘버 
        artist_id = wrap_info.select_one("dt > a")["href"]
        artist_id_num = artist_id[38:-3]

        # [0] : 음원 점수
        # [1] : 팬 증가수 점수
        # [2] : 좋아요 점수
        # [3] : 포토 점수
        # [4] : 비디오 점수
        # 점수들의 평균(이 때 음원 점수는 x4, 팬 증가수 점수는 x2)을 내어 순위를 정함
        score = (
            wrap_info.select_one("dd.consumer_list > table > tbody > tr")
            .text.strip()
            .split("\n")
        )

        score = [float(x) for x in score]
        score[0], score[1] = score[0] * 4, score[1] * 2

        average_point = str(round(sum(score) / len(score) / 1.8, 2))

        artists.append(
            {
                "rank": rank,
                "name": name,
                "fan": fan,
                "average_point": average_point,
                "image_url": image_url,
                "artist_id_num" : artist_id_num
            }
        )
    driver.quit()

    return json.dumps(artists)
