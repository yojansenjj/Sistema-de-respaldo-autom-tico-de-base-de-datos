import os
import datetime
import subprocess
from conexion_db import ConexConexion

class RespaldoControlador:
    def __init__(self, carpeta_respaldo="respaldos", carpeta_logs="logs"):
        self.carpeta_respaldo = carpeta_respaldo
        self.carpeta_logs = carpeta_logs
        os.makedirs(carpeta_respaldo, exist_ok=True)
        os.makedirs(carpeta_logs, exist_ok=True)

    def crear_respaldo(self):
        """Genera un respaldo completo de la base de datos"""
        try:
            conexion = ConexConexion()
            nombre_bd = conexion.database
            fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nombre_archivo = f"{nombre_bd}_{fecha_actual}.sql"
            ruta_respaldo = os.path.join(self.carpeta_respaldo, nombre_archivo)

            # 🔹 Comando mysqldump
            comando = f'mysqldump -u {conexion.user} -p{conexion.password} {nombre_bd} > "{ruta_respaldo}"'
            resultado = subprocess.run(comando, shell=True)

            if resultado.returncode == 0:
                self._registrar_log(f"✅ Respaldo exitoso: {ruta_respaldo}")
                print(f"✅ Respaldo creado en: {ruta_respaldo}")
                return True
            else:
                self._registrar_log("❌ Error al ejecutar mysqldump.")
                print("❌ Error al crear respaldo.")
                return False

        except Exception as e:
            self._registrar_log(f"❌ Error inesperado: {e}")
            print(f"❌ Error inesperado: {e}")
            return False

    def _registrar_log(self, mensaje):
        """Guarda mensajes en el archivo de log"""
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file = os.path.join(self.carpeta_logs, "respaldo_log.txt")

        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"[{fecha}] {mensaje}\n")