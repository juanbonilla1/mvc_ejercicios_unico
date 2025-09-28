from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('biblioteca_virtual', __name__, template_folder='templates')

@bp.before_app_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM biblioteca_virtual ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('biblioteca_virtual_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        anio = request.form.get('anio')
        genero = request.form.get('genero')
        conn = get_db()
        conn.execute(
            "INSERT INTO biblioteca_virtual (titulo, autor, anio, genero) VALUES (?, ?, ?, ?)",
            (titulo, autor, anio, genero,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('biblioteca_virtual.listado'))
    return render_template('biblioteca_virtual_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM biblioteca_virtual WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('biblioteca_virtual.listado'))
