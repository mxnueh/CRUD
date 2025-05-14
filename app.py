import pyodbc
import time
import datetime
from tabulate import tabulate

def get_connection():
    return pyodbc.connect(
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-EK6KQLL\MSSQLSERVER_2022;'
        r'DATABASE=crud_usuarios;'
        r'Trusted_Connection=yes;'
    )

cnxn = get_connection()
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM usuarios")
estudiantes = cursor.fetchall()

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

    print("== Se le asigno una fecha de creacion a su usuario ==")
    time.sleep(1)

    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, creado_en) VALUES (?, ?, ?)", (nombre, email, creado_en))
    cnxn.commit()

    print("Recopilacion de datos ingresados")
    print(f"- Nombre: {nombre}\n- Correo: {email}\n- Fecha de creación: {creado_en}")


elif choice == 2:
    print("BUSQUE EL USUARIO AL QUE DESEA REALIZARLE LOS CAMBIOS\n--------------------------------------")

    nombre = input("Ingrese el nombre: ")
    time.sleep(1)

    cnxn = get_connection()
    cursor = cnxn.cursor()
    query = "SELECT nombre, email, creado_en FROM usuarios WHERE nombre = ?"
    cursor.execute(query, (nombre))

    row = cursor.fetchone()

    if row:
        print(f"\nNombre: {row.nombre}\nEmail: {row.email}\nCreado en: {row.creado_en}\n")

        time.sleep(1)

        print("MODIFIQUE CADA CAMPO DEL USUARIO\n--------------------------------------")

        n_nombre = input("Ingrese el nuevo nombre: ")
        n_email = input("Ingrese el nuevo email: ")

        cursor.execute("UPDATE usuarios SET nombre = ?, email = ? WHERE nombre = ?", (n_nombre, n_email, nombre))
        cnxn.commit()
        cnxn.close()

        time.sleep(1)
        print("LOS CAMBIOS SE REALIZARON CON EXITO")
    else:
        print("\nERROR!. Usuario no encontrado.")

elif choice == 3:
    print("BUSQUE AL USUARIO EN BASE A SU NOMBRE\n-----------------------------")
    nombre = input("Ingrese el nombre de usuario a eliminar")

    time.sleep(1)

    print(f"ESTE ES EL USUARIO A ELIMINAR\n-----------------------------\n- Nombre: {nombre}")

    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE nombre = ?", (nombre))
    cnxn.commit()

    print("EL USUARIO HA SIDO ELIMINADO CON EXITO")

elif choice == 4:
    print("MOSTRANDO DATOS\n-----------------------")

    cnxn = get_connection()
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    
    table = cursor.fetchall()

    data = [[i.nombre, i.email, i.creado_en]  for i in table]
    headers = ["Nombre", "Correo", "Fecha"]

    print(tabulate(data, headers=headers, tablefmt="grid"))

else: 
    print("El programa ha cerrado.")



cnxn.close()