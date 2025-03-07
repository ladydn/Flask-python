from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = [ 'comprar cafe', 'enviar solicitud de compra', 'entregar video a productor']

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response

@app.route("/hello")
def home():
    user_ip = request.cookies.get("user_ip")
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('base_static.html', **context)

