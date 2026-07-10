#crie uma rota q peça um numero e mostre na tela se é impar ou par 

from flask import Flask

app = Flask(__name__)

@app.route("/numero/<int:num>")
def numero(num):
    if num % 2 == 0: #se o resto da divisão do numero por 2 for igual a 0, então é par 
        return f"O número {num} é um número par."
    else:
        return f"O número {num} é um número ímpar."
    
if __name__ == "__main__":
    app.run(debug=True)

# numero  % 2 == 0, pega o resto da divisão do numero por 2, se for igual a 0, então é par, se não for igual a 0, então é ímpar.