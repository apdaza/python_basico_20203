from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<nombre>')
def success(nombre):
    return "Bienvenido %s" % nombre

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nombre']
        return redirect(url_for('success', nombre = usuario))
    else:
        usuario = request.args.get['nombre']
        return redirect(url_for('success', nombre = usuario))

if __name__ == "__main__":
    app.run(debug=True)
