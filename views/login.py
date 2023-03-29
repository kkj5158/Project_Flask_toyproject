from flask import Blueprint, jsonify, render_template, request
from model import db
from model import cursor

# 루트 url 
bp = Blueprint('login', __name__, url_prefix='/login')
# localhost:5000/login


# # localhost:5000/login
@bp.route('/') # -> localhost:5000
def index():

   return render_template('login.html')
# 
# localhost:5000/login/join
@bp.route('/join')
def home():
    return render_template('join.html')

@bp.route('/join' , methods=['POST'])
def join_post():

    id_recive = request.form['id_give']
    password_recive = request.form['password_give']
    email_recive = request.form['email_give']
    address_recive = request.form['address_give']
    phone_recive = request.form['phone_give']


    print(id_recive, password_recive, email_recive, address_recive, phone_recive)
    return jsonify({'msg':'회원가입완료'})


