from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    tasks = []
    with open("Dados.txt", "r") as arquivo:
        for line in arquivo:
            origem, destino, peso = line.split()
            if origem not in tasks:
                tasks.append(origem)
                print(tasks)
    return render_template('index.html', task=tasks)


app.run(debug=True)
