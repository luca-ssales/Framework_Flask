#Crie uma rota que recebe seu nome na URL e exibe uma mensagem de boas-vindas personalizada na tela do navegador.

from flask import Flask

app = Flask(__name__)

@app.route("/welcome/<name>") #a rota da page/ a varivel na url
def welcome(name): # tras a page (variavel) da url e exibe na tela do navegador
    return f"Bem-vindo(a), {name}! 👋🏻" #f string e colocou a variavel entre chaves {}

if __name__ == "__main__":
    app.run(debug=True)