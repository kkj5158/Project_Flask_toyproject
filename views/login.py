from flask import Blueprint, jsonify, redirect, render_template, request, url_for

import certifi
import pymysql

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


# 루트 url 
bp = Blueprint('login', __name__, url_prefix='/login')
# localhost:5000/login


# # localhost:5000/login
@bp.route('/') # -> localhost:5000
def login():

   msg = request.args.get("msg")

   

   return render_template('login.html', msg=msg)
# 
# localhost:5000/login/join

@bp.route('/login', methods=['POST'])
def api_login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    print("로그인 진입")

    # 회원가입 때와 같은 방법으로 pw를 암호화합니다.
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # id, 암호화된pw을 가지고 해당 유저를 찾습니다.

    sql = 'SELECT user_id, pw FROM artist.user where user_id=%s and pw = %s'

    val =(id_receive, pw_receive)
    
    cursor.execute(sql,val)
    
    result = cursor.fetchone()

    print(result)



    # 찾으면 JWT 토큰을 만들어 발급합니다.
    if result is not None:
        # JWT 토큰에는, payload와 시크릿키가 필요합니다.
        # 시크릿키가 있어야 토큰을 디코딩(=풀기) 해서 payload 값을 볼 수 있습니다.
        # 아래에선 id와 exp를 담았습니다. 즉, JWT 토큰을 풀면 유저ID 값을 알 수 있습니다.
        # exp에는 만료시간을 넣어줍니다. 만료시간이 지나면, 시크릿키로 토큰을 풀 때 만료되었다고 에러가 납니다.
        payload = {
            'id': id_receive,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
        }
        
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

        # token을 줍니다.
        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})





@bp.route('/join')
def join():
    return render_template('join.html')

@bp.route('/join/register' , methods=['POST'])
def join_post():

    id_recive = request.form['id_give']
    password_recive = request.form['password_give']
    email_recive = request.form['email_give']
    address_recive = request.form['address_give']
    phone_recive = request.form['phone_give']
    name_recive = request.form['name']


    pw_hash = hashlib.sha256(password_recive.encode('utf-8')).hexdigest()

    sql = "INSERT INTO `artist`.`user`(`id`,`name`,`user_id`,`pw`,`email`,`address`,`tel`) VALUES (get_seq('userSeq'),%s,%s,%s,%s,%s,%s)"

    val = (name_recive,id_recive,password_recive,email_recive,address_recive,phone_recive)

    cursor.execute(sql,val)

    db.commit()

   
    print(id_recive, password_recive, email_recive, address_recive, phone_recive)
    return jsonify({'msg':'회원가입완료'})


