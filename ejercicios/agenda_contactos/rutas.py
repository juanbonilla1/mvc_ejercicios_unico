from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('agenda_contactos', __name__, template_folder='templates')

@bp.before_app_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM agenda_contactos ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('agenda_contactos_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')
        direccion = request.form.get('direccion')
        correo = request.form.get('correo')
        conn = get_db()
        conn.execute(
            "INSERT INTO agenda_contactos (nombre, telefono, direccion, correo) VALUES (?, ?, ?, ?)",
            (nombre, telefono, direccion, correo,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('agenda_contactos.listado'))
    return render_template('agenda_contactos_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM agenda_contactos WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('agenda_contactos.listado'))
