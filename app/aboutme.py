from app import app


@app.route("/")
def index():
    return "Hello World!"


@app.route("/aboutme")
def about_me():
    me = {"first_name": "Nathan",
          "last_name": "Newport",
          "hobby": "Cool things"}
    return me
