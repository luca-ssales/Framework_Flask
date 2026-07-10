#peçam dois números e mostre na tela do navegador.

from flask import Flask, request

app = Flask(__name__)

@app.route("/numero/<int:num1>/<int:num2>") #a rota da page/ a varivel na url
def numero(num1, num2):
    return f"Os números digitados foram: {num1} e {num2}. A soma deles é: {num1 + num2}" #f string e colocou a variavel entre chaves {}

if __name__ == "__main__":
    app.run(debug=True)