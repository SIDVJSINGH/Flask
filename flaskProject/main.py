from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/404 found coders"  # username is "root" for xampp by default and password is "" nothing
# create the extension and initialize it
db = SQLAlchemy(app)


class Contacts(db.Model):
    """
    name, email, phone, message, srno, date_skey
    """
    # nullable is True by default
    srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(255), nullable=False)
    date = db.Column(db.String(20), nullable=True)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post")
def post():
    return render_template("posts/post1.html")

@app.route("/post1")
def post1():
    return render_template("posts/post1.html")

@app.route("/post2")
def post2():
    return render_template("posts/post2.html")

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        """ Add entry to DB """
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, email=email, phone=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()


    return render_template("contact.html")


if __name__ == "__main_":
    app.run(debug=True, port=8080)