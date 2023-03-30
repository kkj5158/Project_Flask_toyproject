import certifi
from flask import Blueprint, redirect, render_template, request, url_for
import jwt

import pymysql
import json

ca=certifi.where()

# JWT 토큰을 만들 때 필요한 비밀문자열입니다. 아무거나 입력해도 괜찮습니다.
# 이 문자열은 서버만 알고있기 때문에, 내 서버에서만 토큰을 인코딩(=만들기)/디코딩(=풀기) 할 수 있습니다.
SECRET_KEY = 'SPARTA'


# JWT 패키지를 사용합니다. (설치해야할 패키지 이름: PyJWT)
import jwt

# 토큰에 만료시간을 줘야하기 때문에, datetime 모듈도 사용합니다.
import datetime

# 회원가입 시엔, 비밀번호를 암호화하여 DB에 저장해두는 게 좋습니다.
# 그렇지 않으면, 개발자(=나)가 회원들의 비밀번호를 볼 수 있으니까요.^^;
import hashlib



db = pymysql.connect(
        host="artist.cqjw1iajcspu.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user="admin",
        passwd="qlgodrl12",
        db="artist",
        charset="utf8",
    )

cursor = db.cursor()

bp = Blueprint("index", __name__, url_prefix="/")


@bp.route("/")
def home():
    token_receive = request.cookies.get('mytoken')

    try:
      payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

      sql = "SELECT id FROM artist.user where user_id = %s"

      with db:
           with db.cursor as cur:
                cur.execute(sql, (payload['id']))

                result = cur.fetchall()

                for data in result:
                     print(data)



      return render_template('login.html', nickname=result[0])
   
    except jwt.ExpiredSignatureError:
      return redirect(url_for("login.login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
      return redirect(url_for("login.login", msg="로그인 정보가 존재하지 않습니다."))


    return render_template("index.html")

@bp.route("/rank")
def rank():



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
