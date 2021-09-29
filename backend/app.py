from flask import Flask, render_template, request ,jsonify

app = Flask(__name__)

@app.route("/signup/",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        return jsonify({email:password})
    return render_template('signup.html')
    

# @app.route("/api/",method=["POST"])
# def signup():
#     return render_template('signup.html')

@app.route("/signin/",methods=["POST"])
def signin():
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)
