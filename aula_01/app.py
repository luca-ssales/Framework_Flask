# Aula 01- Instalando o flask 
# pip inmstall flask


from flask import Flask 

app = Flask(__name__)

@app.route("/cadastro") #cria uma orota para a página de cadastro
def cadastro():
    return "Welcome to the registration page!"

@app.route("/login") #cria uma rota para a página de login
def login():
    return "Welcome to the login page!"

if __name__ == "__main__":
    app.run()

