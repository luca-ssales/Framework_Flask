#aula 03- criando url Dinamicas 

from flask import Flask 

app = Flask(__name__) 

@app.route("/hello/") #cria uma rota para a página inicial, e com a barra no final, o usuário pode acessar a rota sem precisar digitar o nome
@app.route("/hello/<name>")
def hello(name=""):
    return f"<h1>Hello, {name}!</h1>"


@app.route("/blog/") #cria uma rota para a página de usuário, e com a barra no final, o usuário pode acessar a rota sem precisar digitar o nome
@app.route("/blog/<string:post_id>") #o <int:post_id> é um parâmetro que recebe um valor inteiro, e o nome do parâmetro é post_id
def blog(post_id=None):
    if post_id is None:
        return "<h1>Welcome to the Blog!</h1>"
    else:
        return f"<h1>Blog Post ID: {post_id}</h1>"


if __name__ == "__main__":
    app.run(debug=True) 
    
    