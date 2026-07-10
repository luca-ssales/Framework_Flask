from flask import Flask

app = Flask("__name__")

@app.route("/aluno/<aluno>")
def monstrar_aluno(aluno):
    if aluno == "lucas":
        return '''
        <h3> Lucas Sales </h3>
        <p>
        Idade: 20 <br>
        Curso: Engenharia de Software <br>
        Cidade: São Paulo (SP)
        </p>
'''
    elif aluno == "joao":
        return '''
        <h3> João Carlos </h3>
        <p>
        Idade: 25 <br>
        Curso: Ads <br>
        Cidade: Natal (RS)
        </p>
'''
    elif aluno == "maria":
        return '''
        <h3> Maria Helena </h3>
        <p>
        Idade: 45 <br>
        Curso: Tecnologia da Informação <br>
        Cidade: Rio de Janeiro (RJ)
        </p>
'''
    elif aluno == "laura":
        return '''
        <h3> Laura Santos </h3>
        <p>
        Idade: 15 <br>
        Curso: Cursando Ensino Médio <br>
        Cidade: Rondonia (RO)
        </p>
'''
    else:
        return "Aluno não encontrado!"

if __name__ == "__main__":
    app.run(debug=True)