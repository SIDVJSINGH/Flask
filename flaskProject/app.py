from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
# create the extension and initialize it
db = SQLAlchemy(app)


class Contacts(db.Model):
    """
    name, email, phone, message, srno, date_skey
    """
    # nullable is True by default
    # srno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(12),primary_key=True, nullable=False)
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
        # name = request.form.get('name')
        # email = request.form.get('email')
        # phone = request.form.get('phone')
        # message = request.form.get('message')

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        entry = Contacts(name=name, email=email, phone=phone, message=message, date=datetime.now())
        # db.session.add(entry)
        # db.session.commit()

        # Push to the Database
        try:
            db.session.add(entry)
            db.session.commit()
            return redirect('/contact')
        except:
            return "Error sending info"

    # contacts = Contacts.query.order_by(Contacts.date)
    return render_template("contact.html")


app.run(debug=True)