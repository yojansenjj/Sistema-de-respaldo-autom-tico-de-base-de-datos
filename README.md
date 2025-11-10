# 🗄️ Sistema de Respaldo Automático de Base de Datos

Proyecto desarrollado en **Python** para generar respaldos automáticos de una base de datos **MySQL**.  
El sistema crea copias de seguridad en formato `.sql` y registra cada acción en un archivo de logs.

---

## ⚙️ Tecnologías utilizadas
- Python 3  
- MySQL / XAMPP  
- PyMySQL  
- mysqldump  

---

## 🚀 Cómo ejecutar
1. Clona o descarga el repositorio.  
2. Configura tus credenciales en `conexion_db.py`:
   ```python
   self.user = "root"
   self.password = ""
   self.host = "localhost"
   self.database = "soporte_tecnico"

👨‍💻 Autor

Yojansen Oliveros
Desarrollador Python | Automatización | Gestión de datos
