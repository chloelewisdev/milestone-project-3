import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if username already exists 
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Oops, that username already exists! Please try again with a different username")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Welcome! You have now signed up")
        return redirect(url_for("my_tips", username=session["user"]))

    return render_template("signup.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                            request.form.get("username")))
                    return redirect(url_for("my_tips", username=session["user"]))
                    
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("login.html")


@app.route("/log_out")
def log_out():
	flash("You have now been logged out")
	session.pop("user")
	return redirect(url_for("log_in"))


@app.route("/tips")
def tips():
    tips = list(mongo.db.tips.find())
    return render_template("tips.html", tips=tips)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    #tips = list(mongo.db.tips.find({"$text": {"$search": query}}))
    query_string = {'$regex': ".*{0}.*".format(query), '$options': 'i'}
    tips = list(mongo.db.tips.find({
        "$or": [
            {"category_name": query_string}, 
            {"tip_suggestion": query_string},
            {"tip_details": query_string}
            ]
    }))

    return render_template("tips.html", tips=tips)


@app.route("/add_tip", methods=["GET", "POST"])
def add_tip():
    if request.method == "POST":
        tip = {
            "category_name": request.form.get("category_name"),
            "tip_suggestion": request.form.get("tip_suggestion"),
            "tip_details": request.form.get("tip_details"),
            "created_by": session["user"]
        }
        mongo.db.tips.insert_one(tip)
        flash("Thank you...your working from home tip has now been added to our community board below!")
        return redirect(url_for("tips"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_tip.html", categories=categories)


@app.route("/edit_tip/<tip_id>", methods=["GET", "POST"])
def edit_tip(tip_id):
    if request.method == "POST":
        tip_update = {
            "category_name": request.form.get("category_name"),
            "tip_suggestion": request.form.get("tip_suggestion"),
            "tip_details": request.form.get("tip_details"),
            "created_by": session["user"]
        }

        mongo.db.tips.update({"_id": ObjectId(tip_id)}, tip_update)
        flash("Thanks, you have succesfully updated your tip")
        return redirect(url_for("tips"))

    tip = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_tip.html", tip=tip, categories=categories)


@app.route("/delete_tip/<tip_id>")
def delete_tip(tip_id):
    mongo.db.tips.remove({"_id": ObjectId(tip_id)})
    flash("You have successfully removed your tip from the community board")
    return redirect(url_for("tips"))


@app.route("/my_tips/<username>", methods=["GET", "POST"])
def my_tips(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        tips = list(mongo.db.tips.find().sort("_id", 1))
        return render_template("mytips.html", username=username, tips=tips)

    return redirect(url_for("log_in"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
