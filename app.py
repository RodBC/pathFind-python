from flask import Flask, render_template, request
from dijkstra import *

app = Flask(__name__)

def getData():
    airports = []
    with open("Dados.txt", "r") as arquivo:
        for line in arquivo:
            origem, destino, peso = line.split()
            if origem not in airports:
                airports.append(origem)
    return airports

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        origem = request.form.get('origem').upper()
        destino = request.form.get('destino').upper()
        resultado = g.calcula_caminho(origem, destino)
        return render_template('index.html', airports=getData(), resultado=resultado)
    else:    
        return render_template('index.html', airports=getData())


app.run(debug=True)
