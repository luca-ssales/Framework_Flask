#aula 04- Construção de URL 

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/login" )
def login():
    return '''
    <h1>Voce precisa fazer um login!</h1>
    <p>não tem login? vá para /cadastro</p>
'''

@app.route("/cadastro")
def cadastro():
    return "<h1>Voce esta na pagina de cadastro!</h1>"
    
@app.route("/google")
def google():
    return redirect("https://www.google.com") #me redireciona para o google, mas poderia ser qualquer site, e não precisa ser necessariamente um site externo, poderia ser uma rota interna do próprio site

if __name__ == "__main__":
    app.run(debug=True)
