from flask import Flask, request, render_template, session
from flask import redirect, make_response, jsonify
from functools import wraps
import os

from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, verify_jwt_in_request
from flask_jwt_extended import JWTManager, get_jwt_identity, get_jwt
from flask_jwt_extended import set_access_cookies


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secretkey"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
jwt = JWTManager(app)
jwt.init_app(app)
app = Flask(__name__)
app.secret_key = "secretkey"
app.config["UPLOADED_PHOTOS_DEST"] = "static"
app.config["JWT_SECRET_KEY"] = "secretkey"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_COOKIE_CSRF_PROTECT"] = False

jwt = JWTManager(app)
jwt.init_app(app)

books = [
    {
        "id": 1,
        "author": "Joe Reis and Matt Housley",
        "country": "USA",
        "language": "English",
        "title": "Fundamentals of Data Engineering: Plan and Build Robust Data Systems",
        "year": 2022,
    },
        {
        "id": 2,
        "author": "Dave Thomas and Andy Hunt",
        "country": "USA",
        "language": "English",
        "title": "The Pragmatic Programmer: Your Journey to Mastery (20th Anniversary Edition)",
        "year": 2020,
    },
    {
        "id": 3,
        "author": "Alan Beaulieu",
        "country": "USA",
        "language": "English",
        "title": "Learning SQL: Generate, Manipulate, and Retrieve Data 3rd Edition",
        "year": 2020,
    }
]

users = [
    {"username": "admin", "password": "admin", "role": "admin"},
    {"username": "reader", "password": "reader", "role": "reader"}
]


def admin_required(fn):
   @wraps(fn)
   def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        # FOR DEBUG PURPOSES ONLY
        # return jsonify(claims)
        if claims['role'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return jsonify(msg='Admins only!'), 403
   return wrapper


def checkUser(username, password):
    for user in users:
        if username in user["username"] and password in user["password"]:
            return {"username": user["username"], "role": user["role"]}
    return None


@app.route("/", methods=["GET"])
def firstRoute():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        validUser = checkUser(username, password)
        if validUser != None:
            # set JWT token
            user_claims = {"role": validUser["role"]}
            access_token = create_access_token(
                username, fresh=False, expires_delta=False, 
                additional_claims=user_claims
                )

            response = make_response(
                render_template(
                    "index.html", title="books", username=username, books=books
                )
            )
            response.status_code = 200
            set_access_cookies(response, access_token)
            return response

    return render_template("register.html")


@app.route("/logout")
def logout():
    return "Logged Out of Books"


@app.route("/books", methods=["GET"])
@jwt_required()
def getBooks():
    try:
        username = get_jwt_identity()
        return render_template('books.html', username=username, books=books)
    except:
        return render_template("register.html")


@app.route("/addbook", methods=["GET", "POST"])
@jwt_required()
@admin_required
def addBook():
    username = get_jwt_identity()
    if request.method == "GET":
        return render_template("addBook.html", username=username)
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        year = request.form.get("year")
        id = request.form.get("id")
        newbook = {"id": id, "author": author, "title": title, "year": year}
        books.append(newbook)
        return render_template(
            "books.html", books=books, username=username, title="books"
        )
    else:
        return 400


@app.route("/addimage", methods=["GET", "POST"])
@jwt_required()
@admin_required
def addimage():
    if request.method == "GET":
        return render_template("addimage.html")
    elif request.method == "POST":
        image = request.files["image"]
        id = request.form.get("number")
        imagename = "image" + id + ".png"
        image.save(os.path.join(app.config["UPLOADED_PHOTOS_DEST"], imagename))
        print(image.filename)
        return "image loaded"

    return "all done"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
