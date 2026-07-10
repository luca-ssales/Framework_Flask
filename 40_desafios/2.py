#Crie uma rota sobre voce

from flask import Flask

app = Flask(__name__)

@app.route("/sobre")
def sobre(): #<br> é uma tag de quebra de linha, que serve para quebrar a linha e pular para a próxima linha
    return '''
    <h1>Olá, meu nome é Lucas👋🏻</h1>
    <p>Tenho 19 anos e atualmente estou cursando Analise e Desenvolvimento de Sistemas(ADS). Tenho <br>
     um forte interresse na area de font end, mas támbem estou buscando
    conhecimentos em back end usando python, <br>      
    e nesses desafios, estou aprendendo a usar o framework chamado Flask, que é um micro framework para desenvolvimento web em Python. <br>

    <h4>👨🏻‍💻 Tecnologias que estou estudando: ⌨️</h4>
    <p>
    -HTML <br>
    -CSS <br>
    -JavaScript <br>
    -Python <br>
    -Flask <br>
    -Pygame <br>
    -SQL <br>
    -GitHub.
    </p>

    Guarulhos, 2026

    '''
if __name__ == "__main__":
    app.run(debug=True)