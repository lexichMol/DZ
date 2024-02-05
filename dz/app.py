from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, session




app = Flask(__name__)

app.secret_key = 'keyhigeh363668ifsgjdgagerFFsdflktgiu'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guest.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rooms.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'

db = SQLAlchemy(app)



class Guest(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    patronymic = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Text, nullable=False)
    mail = db.Column(db.Text)
    in_data = db.Column(db.Text, nullable=False)
    out_data = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return self.surname + " " +  self.name + " " +  self.patronymic


class Rooms(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    number_guests = db.Column(db.Text, nullable=False)
    square = db.Column(db.Text, nullable=False)
    bathroom = db.Column(db.Boolean, nullable=False)
    balcony = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return self.title


class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.type




@app.route("/", methods=['GET', "POST"])
def index():
    print(Guest.query.all())
    if request.method == "POST":

        name = request.form.get("name")
        surname = request.form.get("surname")
        patronymic = request.form.get("patronymic")
        guest = Guest.query.all()

        for i in guest:
            if name == i.name and surname == i.surname and patronymic == i.patronymic:
                return "«такой гость проживает в отеле"

        return "извините, гость с указанными данными не найден"


    else:
        return render_template("index.html")

@app.route("/reg", methods=['GET', "POST"])
def reg():

    if request.method == "POST":

        name = request.form.get("name")
        surname = request.form.get("surname")
        patronymic = request.form.get("patronymic")
        phone_number = request.form.get("phone_number")
        mail = request.form.get("mail")
        in_data = request.form.get("in")
        out_data = request.form.get("out")
        guest = Guest(name=name, surname=surname, patronymic=patronymic, phone_number=phone_number, mail=mail,
                      in_data=in_data, out_data=out_data)
        db.session.add(guest)
        db.session.commit()



        return "номер успешно забронирован"


    else:
        return render_template("reg.html")






if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)