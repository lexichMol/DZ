from flask import Flask, render_template

app = Flask(__name__)

@app.route("/about")
def index():
    return render_template("index.html")

@app.route("/login")
def about_school():
    return render_template("log_in.html")

@app.route("/registration")
def about_class():
    return render_template("reg.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)