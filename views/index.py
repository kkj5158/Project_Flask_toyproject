from flask import Blueprint, render_template

import pymysql
import json


bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/ranking", methods=["GET"])
def index():
    db = pymysql.connect(
        host="artist.cqjw1iajcspu.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user="admin",
        passwd="qlgodrl12",
        db="artist",
        charset="utf8",
    )

    cursor = db.cursor()

    artists = []

    # DB에서 table 전체를 추출해 artists 리스트에 딕셔너리들 추가해서 리턴
    cursor.execute("SELECT * FROM artists")
    table = cursor.fetchall()
    for row in table:
        artists.append(
            {
                "ranking": row[0],
                "name": row[1],
                "fan": row[2],
                "score": row[3],
                "image_url": row[4],
                "id": row[5],
                "members": row[6],
                "debut": row[7],
                "debut_song": row[8],
                "a_type": row[9],
                "company": row[10],
            }
        )

    return json.dumps(artists)
