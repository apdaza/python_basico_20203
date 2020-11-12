from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hola/<nombre>')
def hola(nombre):
    diccionario = {'python' : 'excelente', 'java' : 'bueno pero complejo', 'php' : 'facil'}
    return render_template('lenguajes.html', usuario = nombre, lenguajes = diccionario)

if __name__ == "__main__":
    app.run(debug = True)