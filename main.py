from flask import *
from repository import user_repository
import psycopg2

app = Flask(__name__)
app.secret_key = "kutyafule"


@app.route("/registration", methods=['POST'])
def register_user():
    user_dict = request.get_json(force=True)
    first_name = user_dict["firstName"]
    last_name = user_dict["lastName"]
    email = user_dict["email"]
    password = user_dict["password"]
    address = user_dict["address"]
    phone_number = user_dict["phoneNum"]

    try:
        user_repository.insert_user(first_name, last_name, email, password, address, phone_number)
    except psycopg2.IntegrityError:
        return "duplicateEmail"
    return "Success"


@app.route("/login", methods=['POST'])
def login_user():
    email_dict = request.get_json(force=True)
    email = email_dict["email"]
    user = user_repository.get_user_by_email(email)
    if user is None:
        return "userNotFound"
    return jsonify(user)


@app.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = user_repository.get_user_by_id(user_id)
    if user is None:
        return "userNotFound"
    return jsonify(user)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
