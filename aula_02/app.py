#aula 02 - criando rotas e configurações 

from flask import Flask #importando a biblioteca flask


app = Flask(__name__) # inicio

@app.route("/") #cria uma rota para a página inicial
def home():
    return "<h1>Welcome to the Home Page!</h1>"  # h1 do html, mas pode ser apenas um texto simples tb

if __name__ == "__main__":         #port, altera a porta padrão do servidor flask, que é 5000, para 3000
    app.run(debug=True, port=3000) #debug=True permite que o servidor reinicie automaticamente quando houver alterações no código
