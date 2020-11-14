from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# creacion de aplicacion flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.sqlite3'
app.config['SECRET_KEY'] = "12345qwerty"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#creacion objeto de bd
db = SQLAlchemy(app)

class Estudiante(db.Model):
    id = db.Column('estudiante_id', db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    codigo = db.Column(db.String(15))
    correo = db.Column(db.String(50))

    def __init__(self, datos):
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.codigo = datos['codigo']
        self.correo = datos['correo'] 

class Nota(db.Model):
    id = db.Column('nota_id', db.Integer, primary_key = True)
    valor = db.Column(db.Integer)
    estudiante = db.Column(db.Integer)

    def __init__(self, datos):
        self.valor = datos["valor"]
        self.estudiante = datos["estudiante"]

@app.route('/')
def index():
    return render_template("index.html", rows = Estudiante.query.all())

@app.route('/nuevo', methods=['POST', 'GET'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        codigo = request.form['codigo']
        correo = request.form['correo']
        datos = {'nombre': nombre,
                 'apellido': apellido,
                 'codigo': codigo,
                 'correo': correo
                }
        e = Estudiante(datos)
        db.session.add(e)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template("nuevo.html")

@app.route('/editar_estudiante', methods=['POST', 'GET'])
def editar_estudiante():
    if request.method == 'GET':
        id = request.args.get('id')
        e = Estudiante.query.filter_by(id = id).first()
        return render_template("editar.html", e = e)
    else:
        id = request.form['id']
        e = Estudiante.query.filter_by(id = id).first()
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        codigo = request.form['codigo']
        correo = request.form['correo']
        e.nombre = nombre
        e.apellido = apellido
        e.codigo = codigo
        e.correo = correo
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/eliminar_estudiante', methods=['POST', 'GET'])
def eliminar_estudiante():
    if request.method == 'GET':
        id = request.args.get('id')
        e = Estudiante.query.filter_by(id = id).first()
        return render_template("eliminar.html", e = e)
    else:
        id = request.form['id']
        e = Estudiante.query.filter_by(id = id).first()
        db.session.delete(e)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/ver_notas', methods=['POST', 'GET'])
def ver_notas():
    if request.method == 'GET':
        return "notas del estudiante " + str(request.args.get('id'))

@app.route('/agregar_nota', methods=['POST', 'GET'])
def agregar_nota():
    if request.method == 'GET':
        return "agregando nota al estudiante " + str(request.args.get('id'))

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)