from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('foro_comentarios', __name__, template_folder='templates')

@bp.before_app_first_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM foro_comentarios ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('foro_comentarios_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        mensaje = request.form.get('mensaje')
        conn = get_db()
        conn.execute(
            "INSERT INTO foro_comentarios (nombre, mensaje) VALUES (?, ?)",
            (nombre, mensaje,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('foro_comentarios.listado'))
    return render_template('foro_comentarios_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM foro_comentarios WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('foro_comentarios.listado'))
