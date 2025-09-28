from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('gestion_ventas', __name__, template_folder='templates')

@bp.before_app_first_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM gestion_ventas ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('gestion_ventas_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        producto = request.form.get('producto')
        cliente = request.form.get('cliente')
        fecha = request.form.get('fecha')
        total = request.form.get('total')
        conn = get_db()
        conn.execute(
            "INSERT INTO gestion_ventas (producto, cliente, fecha, total) VALUES (?, ?, ?, ?)",
            (producto, cliente, fecha, total,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('gestion_ventas.listado'))
    return render_template('gestion_ventas_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM gestion_ventas WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('gestion_ventas.listado'))
