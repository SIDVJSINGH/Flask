from flask import Flask, render_template, request
from datetime import datetime
from flask_pymongo import PyMongo


# create the app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/blogsite"
# create the extension and initialize it
mongo = PyMongo(app)


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
    if(request.method == 'POST'):
        """ Add entry to DB """
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        try:
            mongo.db.blogContacts.insert_one({
                "date": datetime.now(),
                "name": name,
                "email": email,
                "phone": phone,
                "message": message
                })
        except:
            return render_template("error_page.html")



    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True,port=8080)