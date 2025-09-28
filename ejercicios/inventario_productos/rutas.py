from flask import Blueprint, render_template, request, redirect, url_for
from .modelos.conexion import get_db, init_db

bp = Blueprint('inventario_productos', __name__, template_folder='templates')

@bp.before_app_first_request
def start():
    init_db()

@bp.route('/')
def listado():
    conn = get_db()
    rows = conn.execute('SELECT * FROM inventario_productos ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('inventario_productos_listado.html', items=rows)

@bp.route('/nuevo', methods=['GET','POST'])
def nuevo():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        cantidad = request.form.get('cantidad')
        conn = get_db()
        conn.execute(
            "INSERT INTO inventario_productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
            (nombre, precio, cantidad,)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('inventario_productos.listado'))
    return render_template('inventario_productos_formulario.html')

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    conn = get_db()
    conn.execute('DELETE FROM inventario_productos WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('inventario_productos.listado'))
