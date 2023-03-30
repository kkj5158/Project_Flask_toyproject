from flask import Blueprint, jsonify, render_template, request
import pymysql



db = pymysql.connect(
        host="artist.cqjw1iajcspu.ap-northeast-2.rds.amazonaws.com",
        port=3306,
        user="admin",
        passwd="qlgodrl12",
        db="artist",
        charset="utf8",
    )

cursor = db.cursor()


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


    # db에서 댓글 내용 끌어오기 

    sql = "SELECT comment FROM artist.comment where artist_id = %s"

    val = (artist_id_num)

    cursor.execute(sql,val)

    crows = cursor.fetchall()

    print(crows)



    # DB에서 request 받은 id를 찾아서 해당 정보를 딕셔너리로 바꾸어 리턴
    cursor.execute("SELECT * FROM artists WHERE id = %s", artist_id_num)
    
    # 리스트 <- db 정보 저장 
    row = []

    for x in cursor:
        for y in x:
            row.append(y)

    # for i in range(len(row)):
    #     print(i, row[i])

 # 사전 
    artist = {
        "artist_name": row[1],
        "artist_id" : row[5],
        "img_url": row[4],
        "fan_num": row[2],
        "members": row[6],
        "debut": row[7],
        "debut_song": row[8],
        "a_type": row[9],
        "company": row[10],
    }

    return render_template("artist.html", artist_info=artist , comment = crows)


# localhost:5000/artist/gusetbook 

@bp.route("/guestbook", methods=["POST"])
def guestbook_post():
    comment_receive = request.form['comment_give']
    artist_id = request.form['artist_id']

    # print(artist_id)

    sql = "INSERT INTO `artist`.`comment`(`id`,`comment`,`artist_id`) VALUES(get_seq('artistSeq'),%s,%s);"

    val = (comment_receive, artist_id)

    cursor.execute(sql,val)

    db.commit()


    return jsonify({'msg': '저장 완료'})
