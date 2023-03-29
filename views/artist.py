from flask import Blueprint, jsonify, render_template, request
import pymysql


from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.tt37u6v.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


# 루트
bp = Blueprint("artist", __name__, url_prefix="/artist")


# /artist 경로에서
@bp.route("/", methods=["GET"])
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

    artist_id_num = request.args.get("artist_id_num")

    # DB에서 request 받은 id를 찾아서 해당 정보를 딕셔너리로 바꾸어 리턴
    cursor.execute("SELECT * FROM artists WHERE id = %s", artist_id_num)
    row = []

    for x in cursor:
        for y in x:
            row.append(y)

    for i in range(len(row)):
        print(i, row[i])

    artist = {
        "artist_name": row[1],
        "img_url": row[4],
        "fan_num": row[5],
        "members": row[6],
        "debut": row[7],
        "debut_song": row[8],
        "a_type": row[9],
        "company": row[10],
    }

    return render_template("artist.html", artist_info=artist)


# localhost:5000/artist/gusetbook 

@bp.route("/guestbook", methods=["POST"])
def guestbook_post():
    comment_receive = request.form['comment_give']
    doc = {
        'comment':comment_receive
    }
    db.fan.insert_one(doc)

    return jsonify({'msg': '저장 완료'})

@bp.route("/guestbook", methods=["GET"])
def guestbook_get():
    all_comments = list(db.fan.find({},{'_id':False}))
    return jsonify({'result': all_comments})
