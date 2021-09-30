from flask import Flask, render_template, request ,jsonify
from database_connection.insert_to_db import register_user
import random
from database_connection.insert_to_db import user
app = Flask(__name__)


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97,123)] + [str(i) for i in range(10)]) for _ in range(length) ) 

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
                user_dict = user.find_one({"email":email})
                user_dict.pop("password")
                user_dict.pop("_id")
                if user_data['session_token'] != 0:
                    query ={ "$set": {"session_token":0}}
                    user.update_one({"email":email},query)
                    return jsonify({"error":"Previous Login Exists"})
                session_token =  generate_session_token()
                query ={ "$set": {"session_token":session_token} }
                user.update_one({"email":email},query)
                return jsonify({"token":session_token,"user":user_dict})

                

        return jsonify({"error":"Email Doesnot Exists, Register From Here"})
    return render_template('signin.html')

if __name__=="__main__":
    app.run(debug=True)
