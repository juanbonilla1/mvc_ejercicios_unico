from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('reservas_citas_medicas', __name__, template_folder='templates')

@bp.before_app_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM reservas_citas_medicas ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('reservas_citas_medicas_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        paciente = request.form.get('paciente')
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        motivo = request.form.get('motivo')
        conn = get_db()
        conn.execute(
            "INSERT INTO reservas_citas_medicas (paciente, fecha, hora, motivo) VALUES (?, ?, ?, ?)",
            (paciente, fecha, hora, motivo,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('reservas_citas_medicas.listado'))
    return render_template('reservas_citas_medicas_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM reservas_citas_medicas WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('reservas_citas_medicas.listado'))
