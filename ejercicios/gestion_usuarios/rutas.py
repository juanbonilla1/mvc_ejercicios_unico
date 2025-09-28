from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('gestion_usuarios', __name__, template_folder='templates')

@bp.before_app_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM gestion_usuarios ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('gestion_usuarios_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')
        conn = get_db()
        conn.execute(
            "INSERT INTO gestion_usuarios (nombre, email, contrasena) VALUES (?, ?, ?)",
            (nombre, email, contrasena,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('gestion_usuarios.listado'))
    return render_template('gestion_usuarios_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM gestion_usuarios WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('gestion_usuarios.listado'))
