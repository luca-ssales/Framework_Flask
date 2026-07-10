#crie uma rota que monstre uma contagemd de 1 até n(que seria o numero que o user vai digitar na url) e mostre na tela do navegador.
from flask import Flask

app = Flask(__name__)

@app.route("/numero/<int:num>")
def numero(num):
    numeros = [] #criamos uma lista vazia pra colocar os números que a pessoa digitar
    for nu in range(1, num + 1):  # coloquei +1 pra ir até o número que a pessoa digitar = de 1 até n mais 1
        numeros.append(str(nu)) #esta pegando o num da rota e add com o append na lista vazia, e convertendo pra string pra poder mostrar no navegador
    
    return "<br>".join(numeros)  # return pra mostrar no navegador

if __name__ == "__main__":
    app.run(debug=True)
