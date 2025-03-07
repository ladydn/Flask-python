from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response

@app.route("/hello")
def home():
    user_ip = request.cookies.get("user_ip")
    return "¡Hola, Flask en Linux!, tu IP es {}".format(user_ip)