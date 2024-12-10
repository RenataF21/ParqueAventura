from app import render_template, redirect, request, flash, session, url_for
from app.models.visita import Visita
from app.models.usuario import Usuario
from app import app


@app.route('/nueva', methods=['GET', 'POST'])
def nueva():
    if request.method == 'GET':
        return render_template('nueva.html')
    
    if request.method == 'POST':
        # Crear diccionario con los datos del formulario
        data = {
            'parque': request.form['parque'],
            'rating': request.form['rating'],
            'fecha_de_visita': request.form['fechaDeVisita'],
            'desarrollo': request.form['desarrollo'],
        }

        # Validar los datos
        errores = Visita.validar_visita(data)
        if errores:
            for error in errores:
                flash(error, 'error')
            return render_template('nueva.html', data=data)

        # Crear la visita
        visita_id = Visita.crear(data)
        if visita_id:
            flash('La visita se ha creado exitosamente', 'success')
            return redirect(url_for('dashboard'))
        
        flash('Error al crear la visita', 'error')
        return render_template('nueva.html', data=data)

@app.route('/ver/<int:id>')
def ver(id):
    visita = Visita.obtener_por_id(id)
    if not visita:
        flash('Visita no encontrada', 'error')
        return redirect(url_for('dashboard'))
    
    return render_template('ver.html', visita=visita)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    if Visita.eliminar(id):
        flash('La visita ha sido eliminada exitosamente', 'success')
    else:
        flash('Error al eliminar la visita', 'error')
    return redirect(url_for('dashboard'))

@app.route("/editar/<int:id>")
def editar(id):
    if 'usuario_id' not in session:
        return redirect('/login')
    
    visita = Visita.obtener_por_id(id)
    if visita.organizador != session['usuario_id']:
        flash("No tienes permiso para editar esta visita", "error")
        return redirect(url_for('dashboard'))
    else:
        # Mostrar usuarios que no estén en la visita solamente
        print(visita)
        return render_template("editar.html", data=visita)
    
@app.route("/editar", methods=['POST'])
def editar_visita():
    if 'usuario_id' not in session:
        return redirect('/login')
    
    datos = {
        "id_visita": request.form['id'],
        'parque': request.form['parque'],
        "rating": request.form['rating'],
        "fecha_de_visita": request.form['fechaDeVisita'],
        "detalles": request.form['detalles'],
    }
    Visita.editar(datos)

    flash("La visita ha sido editada exitosamente", "success")
    return redirect(url_for('dashboard'))
