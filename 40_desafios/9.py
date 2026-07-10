from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return '''
    <h3>Alunos matriculados: <br> </h3>
    <p> 
    1- Lucas <br> 
    2- João <br>
    3- Maria <br>
    4- Laura
    </p>
'''
if __name__ == "__main__":
    app.run(debug=True)
