"""
    Guardar y presentar información en las entidades en la base de datos
"""
from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute
# Se crea un proceso repetitivo para ingresar información por teclado,
# de acuerdo a las caracteríticas de la entidad Empleado

lista_empleados = []
bandera = True

while bandera:
    nombre = input("Ingrese nombre del empleado:   ")
    apellido = input("Ingrese apellido del empleado:  ")
    edad = int(input("Ingrese la edad del empleado:    "))
    sueldo = float(input("Ingrese el sueldo del empleado:"))
    lista_empleados.append((nombre, apellido, edad, sueldo))
    salida = input("Desea salir del ciclo, ingres la letra (f): ")
    if salida == 'f':
        bandera = False

print("fin de ingreso de información\n")
for l in lista_empleados:
    cadena_sql = """INSERT INTO Empleado (nombre, apellido, \
    edad, sueldo) VALUES ('%s', '%s', %d, %f);""" % \
    (l[0], l[1], l[2], l[3])
    # ejecutar el SQL
    cursor.execute(cadena_sql)
    # confirmar los cambios
    conn.commit()

"""
# hacer la consulta a la base de datos
cadena_consulta_sql = "SELECT * from Equipo"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print("Presentación de información de la base de datos")
for d in informacion:
    print("Nombre: %s - Siglas:%s - Seguidores: %d - Campeonatos: %d"
    "- Estadio: %s" % (d[0], d[1], d[2], d[3], d[4]))
# cerrar el enlace a la base de datos (recomendado)
cursor.close()
"""