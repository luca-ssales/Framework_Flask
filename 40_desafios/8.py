
from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return '''
    <h1>Welcome to my page!🎊 <br> 

    
    
    
    
    
    '''


if __name__ == "__main__":
    app.run(debug=True)