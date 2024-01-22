from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', "POST"])
def registration():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        login = request.form.get("login")
        psw = request.form.get("password")
        if login == "admin" and psw == "admin":
            return render_template("admin.html")
        else:
            return render_template("user.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/user")
def user():
    return render_template("user.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)