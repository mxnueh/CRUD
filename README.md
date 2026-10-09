# CRUD

Aplicación de consola en Python que realiza operaciones CRUD (crear, leer, actualizar y eliminar) sobre la tabla `usuarios` de una base de datos SQL Server.

## 1. Descripción

Script CLI que se conecta a SQL Server mediante **pyodbc** y presenta un menú interactivo para administrar usuarios del sistema de notificaciones. Los resultados se muestran en tablas con **tabulate**.

## 2. Características

- **Añadir:** registra un usuario con nombre y correo; la fecha de creación se asigna automáticamente.
- **Actualizar:** busca un usuario por nombre y modifica su nombre y correo.
- **Eliminar:** busca un usuario por nombre y lo elimina.
- **Mostrar:** lista todos los usuarios en formato de tabla.
- **Consultas parametrizadas:** todas las sentencias SQL usan parámetros (`?`).

## 3. Tecnologías

- Python 3
- SQL Server
- pyodbc · tabulate

## 4. Requisitos

- Python 3.10 o superior
- SQL Server con una base de datos `System_Notification` y la tabla `usuarios` (`nombre`, `email`, `creado_en`)
- [ODBC Driver 17 for SQL Server](https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server)

```bash
pip install pyodbc tabulate
```

## 5. Configuración

La cadena de conexión está en el método `get_connection()` de `app.py`. Ajusta `SERVER` y `DATABASE` a tu entorno:

```python
r'DRIVER={ODBC Driver 17 for SQL Server};'
r'SERVER=TU_SERVIDOR\TU_INSTANCIA;'
r'DATABASE=System_Notification;'
r'Trusted_Connection=yes;'
```

La conexión usa autenticación de Windows (`Trusted_Connection`).

## 6. Uso

```bash
python app.py
```

```
1. Añadir
2. Actualizar
3. Eliminar
4. Mostrar
5. Cerrar
```

El programa ejecuta una opción por ejecución y luego finaliza.

## 7. Estructura

```
CRUD/
└── app.py    # Clase SCRUD (conexión y consultas) + menú principal
```
