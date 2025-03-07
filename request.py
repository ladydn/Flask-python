from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    # Obtenemos la IP del usuario
    user_ip = request.remote_addr
    return "¡Hola, Flask en Linux!, tu IP es {}".format(user_ip)