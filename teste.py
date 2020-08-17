from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route("/jinja2")
def index_template():
    return render_template("index.html", hello = "Olá Mundo!")

@app.route("/get_teste", methods = ["GET"])
def get_teste():
    primeiro = request.args.get("primeiro", "primeiro padrao ...")
    segundo = request.args.get("segundo")
    # Sim, posso reutilizar...
    return render_template("form_teste.html", primeiro = primeiro, segundo = segundo)

usuarios = [
    {'login': 'aluno1', 'senha': 'azul'},
    {'login': 'aluno2', 'senha': 'vermelho'}
]

@app.route("/login", methods = ["GET"])
def login():
    return render_template("login.html", mensagem = "Entre no sistema")

@app.route("/form_teste", methods = ["PUT", "POST"])
def form_teste():
    login = request.form["login"]
    senha = request.form["password"]
    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("login_ok.html", login = login)
    return render_template("login.html", mensagem = "Login inválido.")

if __name__ == "__main__":
    app.run(port = 8080, debug = True)