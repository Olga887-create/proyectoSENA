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
