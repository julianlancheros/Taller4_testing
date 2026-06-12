import os
import psycopg2
from psycopg2.extras import RealDictCursor


DATABASE_URL = os.environ.get(
    'DATABASE_URL', 
    'postgresql://db_resenas_unilago_user:G8s4D3X5DYhrTXM5MHUpQB5MliYPWzFq@dpg-d8kbnksvikkc73crpgl0-a.frankfurt-postgres.render.com/db_resenas_unilago?sslmode=require'
)

def get_db_connection():
    """Establece la conexión con el servidor PostgreSQL de Render"""
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"❌ Error de conexión a PostgreSQL en Render: {e}")
        return None

def init_db():
    """Crea la tabla de reseñas tecnológicas dentro de la base de datos"""
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                # Creamos la tabla específica para este taller si aún no existe
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS resenas_tecnologicas (
                        id SERIAL PRIMARY KEY,
                        equipo VARCHAR(150) NOT NULL,
                        categoria VARCHAR(50) NOT NULL,
                        calificacion INT NOT NULL,
                        comentario TEXT NOT NULL
                    );
                ''')
                conn.commit()
            print("✅ Tabla 'resenas_tecnologicas' verificada con éxito en Render.")
        except Exception as e:
            print(f"❌ Error al inicializar la tabla: {e}")
        finally:
            conn.close()