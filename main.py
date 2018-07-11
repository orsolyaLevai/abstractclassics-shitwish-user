from flask import *
from repository import userRepository
from controller import userController
import json
import psycopg2
app = Flask(__name__)

app.secret_key = "kutyafule"


@app.route("/registration", methods=['POST'])
def registerUser():
    userdict = request.get_json(force=True)
    firstname = userdict["firstName"]
    lastname = userdict["lastName"]
    email = userdict["email"]
    password = userdict["password"]
    address = userdict["address"]
    phonenumber = userdict["phoneNum"]

    try:
        userRepository.insertUser(firstname, lastname, email, password, address, phonenumber)
    except psycopg2.IntegrityError:
        return "duplicateEmail"
    return "Success"


@app.route("/login", methods=['POST'])
def loginUser():
    emailDict = request.get_json(force=True)
    email = emailDict["email"]
    user = userRepository.getUserByEmail(email)
    if user == None:
        return "userNotFound"
    return jsonify(user)

@app.route("/user/<int:id>", methods=['GET'])
def getUser(id):
    user = userRepository.getUserById(id)
    if user == None:
        return "userNotFound"
    return jsonify(user)



