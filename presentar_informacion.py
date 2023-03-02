"""
    Guardar y presentar información en las entidades en la base de datos
"""
from base_datos import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# hacer la consulta a la base de datos
cadena_consulta_sql = "SELECT * from Empleado"
cursor.execute(cadena_consulta_sql)
# la información resultante se la obtiene del método fetchall de cursor.
informacion = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante
print("Presentación de información de la base de datos")
# variable acumuladoras
suma_edades = 0
suma_sueldos = 0
cadena_presentacion = ""

for d in informacion:
    
    cadena_presentacion = "%sNombre: %s - Apellido: %s - Edad: %d - Sueldo: %.2f\n" % (cadena_presentacion, d[0], d[1], d[2], d[3])
    suma_edades = suma_edades + d[2]
    suma_sueldos = suma_sueldos + d[3]

promedio_edades = float(suma_edades) / len(informacion)
promedio_sueldos = float(suma_sueldos) / len(informacion)
cadena_presentacion = "%s\nPromedio Edades: %.2f\nPromedio Sueldos: %.2f\n" % (cadena_presentacion, promedio_edades, promedio_sueldos)
print(cadena_presentacion)
# cerrar el enlace a la base de datos (recomendado)
cursor.close()
