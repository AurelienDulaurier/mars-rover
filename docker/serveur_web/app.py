# crée un serveur web avec Flask et retourne une page d'accueil

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bonjour, bienvenue sur mon serveur web (j'espere ca marche) 😊"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)