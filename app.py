import pyodbc
import time
import datetime
from tabulate import tabulate

class SCRUD:
    def __init__(self):
        self.cnxn = self.get_connection()
        self.cursor = self.cnxn.cursor()

    def get_connection(self):
        return pyodbc.connect(
            r'DRIVER={ODBC Driver 17 for SQL Server};'
            r'SERVER=DESKTOP-EK6KQLL\MSSQLSERVER_2022;'
            r'DATABASE=System_Notification;'
            r'Trusted_Connection=yes;'
        )

    def search_user(self, nombre):
        self.cursor.execute("SELECT nombre, email, creado_en FROM usuarios WHERE nombre = ?", (nombre,))
        return self.cursor.fetchone()

    def select_all(self):
        self.cursor.execute("SELECT * FROM usuarios")
        return self.cursor.fetchall()

    def close_connection(self):
        self.cnxn.close()


app = SCRUD()

print("\nSISTEMA DE NOTIFICACIONES PARA USUARIO\n-----------------------------")
choice = int(input("""1. Añadir
2. Actualizar
3. Eliminar
4. Mostrar
5. Cerrar

- Que desea hacer: """))

if choice == 1:
    print("INGRESE LOS SIGUIENTES DATOS\n-----------------------------")
    nombre = input("Ingrese el nombre: ")
    email = input("Ingrese el correo: ")

    creado_en = datetime.datetime.now()
    time.sleep(1)

    print("== Se le asignó una fecha de creación al usuario ==")
    time.sleep(1)

    app.cursor.execute(
        "INSERT INTO usuarios (nombre, email, creado_en) VALUES (?, ?, ?)",
        (nombre, email, creado_en)
    )
    app.cnxn.commit()

    print("\nDatos ingresados:")
    print(f"- Nombre: {nombre}\n- Correo: {email}\n- Fecha de creación: {creado_en}")

elif choice == 2:
    print("BUSQUE EL USUARIO AL QUE DESEA REALIZARLE LOS CAMBIOS\n-----------------------------")
    nombre = input("Ingrese el nombre: ")
    time.sleep(1)

    row = app.search_user(nombre)

    if row:
        print(f"\nNombre: {row.nombre}\nEmail: {row.email}\nCreado en: {row.creado_en}\n")
        time.sleep(1)

        print("MODIFIQUE CADA CAMPO DEL USUARIO\n-----------------------------")
        n_nombre = input("Ingrese el nuevo nombre: ")
        n_email = input("Ingrese el nuevo email: ")

        app.cursor.execute(
            "UPDATE usuarios SET nombre = ?, email = ? WHERE nombre = ?",
            (n_nombre, n_email, nombre)
        )
        app.cnxn.commit()

        print("LOS CAMBIOS SE REALIZARON CON ÉXITO")
    else:
        print("ERROR: Usuario no encontrado.")

elif choice == 3:
    print("ELIMINACIÓN DE USUARIO\n-----------------------------")
    nombre = input("Ingrese el nombre de usuario a eliminar: ")
    time.sleep(1)

    row = app.search_user(nombre)

    if row:
        print(f"Se eliminará el siguiente usuario:\n- Nombre: {row.nombre}")
        app.cursor.execute("DELETE FROM usuarios WHERE nombre = ?", (nombre,))
        app.cnxn.commit()
        print("EL USUARIO HA SIDO ELIMINADO CON ÉXITO")
    else: 
        print("ERROR: Usuario no encontrado.")

elif choice == 4:
    print("MOSTRANDO TODOS LOS USUARIOS\n-----------------------------")
    table = app.select_all()
    data = [[i.nombre, i.email, i.creado_en] for i in table]
    headers = ["Nombre", "Correo", "Fecha"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

else:
    print("El programa ha cerrado.")

app.close_connection()
