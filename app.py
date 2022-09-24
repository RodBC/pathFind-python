from flask import Flask, render_template

app = Flask(__name__)


def getData():
    tasks = []
    with open("Dados.txt", "r") as arquivo:
        for line in arquivo:
            origem, destino, peso = line.split()
            if origem not in tasks:
                tasks.append(origem)
    return tasks
@app.route('/')
def index():                
    return render_template('index.html', tasks=getData())


app.run(debug=True)
