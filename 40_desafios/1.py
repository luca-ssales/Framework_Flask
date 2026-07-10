#Crie uma rota que exioba a mensagem Olá, mundo na tela do navegador.

from flask import Flask 

app = Flask(__name__)

@app.route("/home")
def home():
    return "Hello World🌍!"

if __name__ == "__main__":
    app.run(debug=True)