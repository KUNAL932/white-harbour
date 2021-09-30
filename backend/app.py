from flask import Flask, render_template, request ,jsonify, redirect, session, url_for,g
from database_connection.insert_to_db import register_user
from bson.objectid import ObjectId

import random
from database_connection.insert_to_db import user

def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length) ) 

app = Flask(__name__)
app.secret_key= generate_session_token()


@app.route("/signup/",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        if email and password and confirm_password:
            result = register_user(email,password,confirm_password)
            return jsonify(result)
    return render_template('signup.html')
    

'''todo: add api/routes/'''

@app.route("/base/",methods=["GET"])
def base():
    return render_template('base.html')

@app.route("/",methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/signin/",methods=["GET","POST"])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user_data = user.find_one({"email":email})
        if user_data:
            if user_data['password'] == password:
                session.clear()
                session['user'] = email
                return redirect('/')
    return render_template('signin.html')


@app.route("/logout/",methods=["GET"])
def logout():
    if request.method == "GET":
        session.clear()
        return redirect('/signin/')

if __name__=="__main__":
    app.run(debug=True)
