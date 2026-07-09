# teste de url Dinamica

from flask import Flask

app = Flask(__name__)

@app.route("/tabuada/<int:num>")
def tabuada(num): #usei as serquilhas triplas para deixar o código mais legível,
                  #e o f antes das aspas duplas para poder usar as variáveis dentro da string
    return f''' <h1> Sistema de Tabuada 📱 </h1>
    <h2 style="color: #007bff;">Tabuada do {num}</h2> 
    <p>1 x {num} = {1 * num}</p>
    <p>2 x {num} = {2 * num}</p>
    <p>3 x {num} = {3 * num}</p>
    <p>4 x {num} = {4 * num}</p>
    <p>5 x {num} = {5 * num}</p>
    <p>6 x {num} = {6 * num}</p>
    <p>7 x {num} = {7 * num}</p>
    <p>8 x {num} = {8 * num}</p>
    <p>9 x {num} = {9 * num}</p>
    <p>10 x {num} = {10 * num}</p>'''

if __name__ == "__main__":
    app.run(debug=True)