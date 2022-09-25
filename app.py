from flask import Flask, render_template, request
from dijkstra import *

app = Flask(__name__)
lista = []


def getData():
    tasks = []
    with open("Dados.txt", "r") as arquivo:
        for line in arquivo:
            origem, destino, peso = line.split()
            if origem not in tasks:
                tasks.append(origem)
    return tasks

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        origem = request.form.get('origem').upper()
        destino = request.form.get('destino').upper()
        resultado = g.calcula_caminho(origem, destino)
        return render_template('index.html', tasks=getData(), resultado=resultado)
    else:    
        return render_template('index.html', tasks=getData())


app.run(debug=True)
