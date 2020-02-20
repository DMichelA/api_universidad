import web
import app
import json
import csv


class Alumnos:
    app_version = "0.01"  # version de la webapp
    def GET(self):
        try:
            
            datos = web.input()
            if datos['action'] == 'get' and datos['token'] == "1234":
                result1 = []
                result2 = {}
                with open('static/csv/alumnos.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)  # csvfile es una variable_cualquiera
                    for row in reader:
                        result1.append(row)
                        result2['status'] = "200 Ok"
                        result2['app_version'] = self.app_version
                        result2['alumnos'] = result1
                return json.dumps(result2)  # Parsea el diccionario a json

            else:
                result1 = []  # crea array vacio
                result1.append("Token no valido")
                return result1

        except Exception as e:
            result2 = {}  # crea diccionario vacio
            result1['status'] = "Faltan valores"
            return json.dumps(result2)
