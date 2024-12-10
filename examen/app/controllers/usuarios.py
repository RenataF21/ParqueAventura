from app import render_template, request, redirect, session, flash
from app import app, bcrypt
from app.models import Usuario
from app.models import Visita
from datetime import date

#rutas de la aplicacion

@app.route('/')
def login_registro():
    return render_template("login.html")

@app.route("dashboard")
def dashboard():
    if 'usuario_id' not in session:
        return redirect("/")
    visitas = Visita.get.all()
    usuarios = Usuario.get.all()
    return render_template(
        "dashboard.html",
        visitas=visitas,
        usuarios=usuarios
    )

@app.route('/register', methods=['POST'])
def crear_usuario():
    print ("1")
    data = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirmPassword': request.form['confirmPassword']
    }
    if not Usuario.validar_usuario(data):
        print("2")
        return redirect('/')
    else:
        print("3")
        #pw_hash = bcrypt.generate_password_hash(request.form['password'])
        pw_hash = request.form['password']
        data = {
            'nombre': request.form['nombre'],
            'apellido': request.form['apellido'],
            'email': request.form['email'],
            'password': pw_hash
        }
        print(data)
        usuario_id = Usuario.save(data)
        session['usuario_id'] = usuario_id
        return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario.get_by_email(request.form['loginEmail'])
        print(usuario)
        if usuario and bcrypt.check_password_hash(usuario.password, request.form['loginPassword']):
            session['usuario_id'] = usuario.id
            session['nombre'] = usuario.nombre
            return redirect('/dashboard')
        elif not usuario:
            print("Email inválido")
            flash("Email inválido", "succes")
            return redirect('/')
        else:
            flash("Contraseña inválida", "succes")
            return redirect('/')
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear() #limpia datos de la sesión
    return redirect('/')