from flask import Flask
from calculadora import Calculadora

app = Flask(__name__)

@app.route('/suma/<int:v1>/<int:v2>')
def suma(v1, v2):
    c = Calculadora(v1, v2)
    c.sumar()    
    return c.get_respuesta()

@app.route('/resta/<int:v1>/<int:v2>')
def resta(v1, v2):
    c = Calculadora(v1, v2)
    c.restar()    
    return c.get_respuesta()

@app.route('/producto/<int:v1>/<int:v2>')
def producto(v1, v2):
    c = Calculadora(v1, v2)
    c.multiplicar()    
    return c.get_respuesta()

if __name__ == "__main__":
    app.run(debug = True)