from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('registro_cursos_academicos', __name__, template_folder='templates')

@bp.before_app_first_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM registro_cursos_academicos ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('registro_cursos_academicos_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        curso = request.form.get('curso')
        docente = request.form.get('docente')
        creditos = request.form.get('creditos')
        conn = get_db()
        conn.execute(
            "INSERT INTO registro_cursos_academicos (curso, docente, creditos) VALUES (?, ?, ?)",
            (curso, docente, creditos,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('registro_cursos_academicos.listado'))
    return render_template('registro_cursos_academicos_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM registro_cursos_academicos WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('registro_cursos_academicos.listado'))
