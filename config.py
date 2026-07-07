import psycopg2
import os

def conectar():
    try:
        database_url = os.environ.get("DATABASE_URL")
        conexion = psycopg2.connect(database_url)
        return conexion
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a PostgreSQL:", error)
        return None

def desconectar(conexion):
    if conexion is not None:
        conexion.close()
        print("Conexión a PostgreSQL cerrada")

def crear_tabla():
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS empleados (
                id SERIAL PRIMARY KEY,
                identificacion VARCHAR(20) NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                apellido VARCHAR(100) NOT NULL,
                telefono VARCHAR(20),
                cargo VARCHAR(100),
                salario NUMERIC(10,2)
            )
        """)
        conexion.commit()
        cursor.close()
        desconectar(conexion)
        print("Tabla 'empleados' verificada/creada correctamente")
    except (Exception, psycopg2.Error) as error:
        print("Error al crear la tabla:", error)
