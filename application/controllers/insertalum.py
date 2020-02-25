import web # pip intall.web.py
import app
import csv # csv import
import json # json import

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=put&matricula=xx&nombre=xx&&primer_apellido=xx&segundo_apellido=xx&carrera=xxx&token=1234
'''


class Alumnos:


    def GET(self):
        try:
            datos = web.input()
            if datos ['token'] == "1234":
                if datos['action'] == "put":
                    matricula = str(datos['matricula'])
                    nombre = str(datos['nombre'])
                    primer_apellido = str(datos['primer_apellido'])
                    segundo_apellido = str(datos['segundo_apellido'])
                    carrera = str(datos['carrera'])
                    result = [] # crea arreglo (array)
                    result.append(matricula)
                    result.append(nombre)
                    result.append(primer_apellido)
                    result.append(segundo_apellido)
                    result.append(carrera)

                with open('static/csv/alumnos.csv', 'a+', newline='') as csvfile:
                    writer =csv.writer(csvfile) # csvfile es una variable_cualquiera
                    writer.writerow(result)

                result = "matricula,nombre,primer_apellido,segundo_apellido,carrera\n"

                with open('static/csv/alumnos.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile) # csvfile es una variable_cualquiera
                    for row in reader:
                        print(row)
                        fila = str(row['matricula']) + "," + str(row['nombre']) + "," + str(row['primer_apellido']) + "," + str(row['segundo_apellido']) + "," + str(row['carrera'])
                        result+=fila +"\n"
                return result
            else:
                result = [] # crea array vacio
                result.append("Token no valido")
                return result
        except Exception as e:
                result = [] # crea array vacio
                result.append("Faltan valores{}".format(e.args))
                return result