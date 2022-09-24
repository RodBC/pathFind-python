from flask import Flask, render_template, request

app = Flask(__name__)


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
        pass #aqui entra o código do resultado, e um botão para voltar
    else:
        return render_template('index.html', tasks=getData())


app.run(debug=True)
