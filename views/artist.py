from flask import Blueprint, render_template, request
from bs4 import BeautifulSoup


import time
import json


# 루트
bp = Blueprint("artist", __name__, url_prefix="/artist")


# /artist 경로에서
@bp.route("/", methods=["GET"])
def index():
    artist_id_num = request.args.get("artist_id_num")

    # print(artist_id_num)

    default_url = "https://www.melon.com/artist/timeline.htm?artistId="

    html = default_url + artist_id_num

    soup = BeautifulSoup(html, "html.parser")  # SOUP 객체로 웹사이트 변환

    print(soup)

    artists = []

    wrap_info = soup.select_one("#wrap > #cont_wrap > #conts_section > #conts >  div.wrap_dtl_atist > div.dtl_atist clfix")

    print(wrap_info)

   #  img_url = wrap_info.select_one(
   #      "div.wrap_thumb > span.thumb > span.artistImgArea > img"
   #  )["src"]

   #  artist_info = wrap_info.select_one("div.wrap_atist_info")

   #  artist_name = artist_info.select_one("p.title_atist").text

   #  artist_group_names = artist_info.select("a.atistname")["title"]

   #  debut = artist_info.select_one("div.atist_info > span.gubun").text

   #  music = artist_info.select_one(
   #      "div.atist_info > a.btn_play_song > span.songname12"
   #  ).text

   #  a_type = artist_info.select_one("div.atist_info > dd ").next_sibling.text

   #  company = artist_info.select_one(
   #      "div.atist_info > dd "
   #  ).next_sibling.next_sibling.text
    
   #  fan_num = wrap_info.select_one("div.wrap_intst > div.fan_area > span.cnt_span > span.no").text



   #  artists.append(
   #      {
   #          "artist_name": artist_name,
   #          "artist_group_names": artist_group_names,
   #          "debut": debut,
   #          "music": music,
   #          "a_type": a_type,
   #          "company": company,
   #          "img_url" : img_url,
   #          "fan_num" : fan_num

   #      }
   #  )

   #  print(artists)

    return render_template("artist.html")
