from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection, init_db

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_pruebas_de_estres_locust'

# Inicializamos la tabla en Render al arrancar el servidor
init_db()

@app.route('/')
def home():
    """MÓDULO PRINCIPAL - Página 1: Home Page / Index"""
    return render_template('index.html')

@app.route('/resenas', methods=['GET', 'POST'])
def gestion_resenas():
    """MÓDULO DE GESTIÓN - Página 2: Registro y Consulta Embebida"""
    conn = get_db_connection()
    
    # 📥 REGISTRO DE INFORMACIÓN (Método POST)
    if request.method == 'POST':
        equipo = request.form.get('equipo')
        categoria = request.form.get('categoria')
        calificacion = request.form.get('calificacion')
        comentario = request.form.get('comentario')
        
        if equipo and comentario:
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO resenas_tecnologicas (equipo, categoria, calificacion, comentario) VALUES (%s, %s, %s, %s)",
                        (equipo, categoria, int(calificacion), comentario)
                    )
                conn.commit()
                flash('¡Reseña guardada con éxito en PostgreSQL! 💻✨', 'success')
            except Exception as e:
                if conn: conn.rollback()
                flash(f'Error al guardar: {e}', 'error')
            return redirect(url_for('gestion_resenas'))
            
    # 🔍 CONSULTA DE INFORMACIÓN (Método GET)
    resenas = []
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM resenas_tecnologicas ORDER BY id DESC")
                resenas = cur.fetchall()
        except Exception as e:
            print(f"Error al consultar: {e}")
        finally:
            conn.close() # Importante cerrar para que Locust no tumbe la BD por falta de conexiones
            
    return render_template('resenas.html', resenas=resenas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)