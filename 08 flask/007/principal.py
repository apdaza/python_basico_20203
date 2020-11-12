from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from data import operacion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/carga', methods=['POST'])
def carga():
    if request.method == 'POST':
        archivo = request.files['archivo']
        archivo.save(secure_filename(archivo.filename))
        data = [x.split(';') for x in open(archivo.filename).readlines()]
        data = operacion(data)
        return render_template("resultado.html", data = data)

if __name__ == "__main__":
    app.run(debug = True)