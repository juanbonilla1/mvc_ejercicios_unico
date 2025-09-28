from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # Registrar blueprints
    from ejercicios.gestion_usuarios.rutas import bp as gestion_usuarios_bp
    app.register_blueprint(gestion_usuarios_bp, url_prefix='/gestion_usuarios')

    from ejercicios.inventario_productos.rutas import bp as inventario_productos_bp
    app.register_blueprint(inventario_productos_bp, url_prefix='/inventario_productos')

    from ejercicios.reservas_citas_medicas.rutas import bp as reservas_citas_medicas_bp
    app.register_blueprint(reservas_citas_medicas_bp, url_prefix='/reservas_citas_medicas')

    from ejercicios.biblioteca_virtual.rutas import bp as biblioteca_virtual_bp
    app.register_blueprint(biblioteca_virtual_bp, url_prefix='/biblioteca_virtual')

    from ejercicios.registro_cursos_academicos.rutas import bp as registro_cursos_academicos_bp
    app.register_blueprint(registro_cursos_academicos_bp, url_prefix='/registro_cursos_academicos')

    from ejercicios.gestion_ventas.rutas import bp as gestion_ventas_bp
    app.register_blueprint(gestion_ventas_bp, url_prefix='/gestion_ventas')

    from ejercicios.foro_comentarios.rutas import bp as foro_comentarios_bp
    app.register_blueprint(foro_comentarios_bp, url_prefix='/foro_comentarios')

    from ejercicios.agenda_contactos.rutas import bp as agenda_contactos_bp
    app.register_blueprint(agenda_contactos_bp, url_prefix='/agenda_contactos')

    # Ruta principal dentro de la función
    @app.route('/')
    def index():
        return render_template(
            'index.html',
            ejercicios=[
                ('gestion_usuarios', '/gestion_usuarios'),
                ('inventario_productos', '/inventario_productos'),
                ('reservas_citas_medicas', '/reservas_citas_medicas'),
                ('biblioteca_virtual', '/biblioteca_virtual'),
                ('registro_cursos_academicos', '/registro_cursos_academicos'),
                ('gestion_ventas', '/gestion_ventas'),
                ('foro_comentarios', '/foro_comentarios'),
                ('agenda_contactos', '/agenda_contactos'),
            ]
        )

    # 👈 Faltaba devolver la aplicación
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

