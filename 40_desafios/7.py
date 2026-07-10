#receba dois numeros e monstre a soma

from flask import Flask, request

app = Flask(__name__)

@app.route("/soma/<int:num1>/<int:num2>")
def soma(num1, num2):
    return f"A soma dos números {num1} e {num2} é: {num1 + num2}"

if __name__ == "__main__":
    app.run(debug=True)

    