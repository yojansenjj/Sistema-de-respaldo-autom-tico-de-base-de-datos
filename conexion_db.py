# conexion_db.py
import pymysql

class ConexConexion:
    def __init__(self, database="soporte_tecnico"):
        try:
            self.host = 'localhost'
            self.user = 'root'
            self.password = ''
            self.database = database
            self.port = 3306

            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            print(f"✅ Conexión exitosa a la base de datos '{self.database}'")

        except pymysql.MySQLError as e:
            print(f"❌ Error al conectar a MySQL: {e}")
            self.connection = None

    def __enter__(self):
        if self.connection:
            self.micursor = self.connection.cursor()
            return self
        else:
            raise RuntimeError("❌ No se pudo establecer la conexión a la base de datos")

    def __exit__(self, exc_type, exc_value, traceback):
        if hasattr(self, "micursor"):
            self.micursor.close()
        if self.connection:
            self.connection.close()


def probar_conexion():
    try:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="soporte_tecnico"  
        )
        print("✅ Conexión a MySQL exitosa.")
        conexion.close()
        return True
    except Exception as e:
        print("❌ Error al conectar con MySQL:", e)
        return False

if __name__ == "__main__":
    probar_conexion()
