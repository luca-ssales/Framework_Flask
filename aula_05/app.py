#aula 05- Web Arquivos Estaticos 

from flask import Flask

app = Flask(__name__, static_folder="static") #static_folder é o nome da pasta onde estão os arquivos estáticos, 
#como css, js, imagens, etc. Por padrão, o Flask procura a pasta static na raiz do projeto, mas podemos alterar isso 
# passando o nome da pasta como parâmetro para o Flask



if __name__ == "__main__":
    app.run(debug=True)
