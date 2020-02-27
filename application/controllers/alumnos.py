import web  # pip install web.py
import csv  # CSV parser
import json  # json parser

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=get&token=1234

    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=searh&token=1234&matricula=xxx

    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=put&matricula=xx&nombre=xx&&primer_apellido=xx&segundo_apellido=xx&carrera=xxx&token=1234

    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=delete&token=1234&matricula=xxx

    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=update&token=1234&matricula=xxx
'''


class Alumnos:

    app_version = "0.5.0"  # version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los data

    def __init__(self):  # Método inicial o constructor de la clase
        pass  # Simplemente continua con la ejecución

    def GET(self):
        try:
            data = web.input()  # recibe los data por la url
            if data['token'] == "1234":  # valida el token que se recibe por url
                if data['action'] == 'get':  # evalua la acción a realizar
                    result = self.actionGet(self.app_version, self.file)  # llama al metodo actionGet(), y almacena el resultado
                    return json.dumps(result)  # Parsea el diccionario result a formato json
                elif data['action'] == 'search':
                    matricula=data['matricula']
                    result = self.actionSearch(self.app_version, self.file,matricula)
                    return json.dumps(result)
                elif data['action'] == 'put':
                    matricula=int(data['matricula'])
                    nombre=str(data['nombre'])
                    primer_apellido=str(data['primer_apellido'])
                    segundo_apellido=str(data['segundo_apellido'])
                    carrera=str(data['carrera'])
                    alumno = [] # crea arreglo (array)
                    alumno.append(matricula)
                    alumno.append(nombre)
                    alumno.append(primer_apellido)
                    alumno.append(segundo_apellido)
                    alumno.append(carrera)
                    result = self.actionPut(self.app_version, self.file, matricula)
                    return json.dumps(result)
                elif data['action'] == 'delete':
                    matricula = data['matricula']
                    result = self.actionDelete(self.app_version,self.file, matricula)
                    return json.dumps(result)
                #elif data['action'] == 'update':


                else:
                    result = {}  # crear diccionario vacio
                    result['app_version'] = self.app_version  # version de la webapp
                    result['status'] = "Command not found"
                    return json.dumps(result)  # Parsea el diccionario result a formato json
            else:
                result = {}  # crear diccionario vacio
                result['app_version'] = self.app_version  # version de la webapp
                result['status'] = "Invalid Token"
                return json.dumps(result)  # Parsea el diccionario result a formato json
        except Exception as e:
            print("Error")
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args))
            result['app_version'] = self.app_version  # version de la webapp
            result['status'] = "Values missing, sintaxis: alumnos?action=get&token=XXXX"
            return json.dumps(result)  # Parsea el diccionario result a formato json

    @staticmethod
    def actionGet(app_version, file):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status
            
            with open(file, 'r') as csvfile:  # abre el archivo en modo lectura
                reader = csv.DictReader(csvfile)  # toma la 1er fila para los nombres
                alumnos = []  # array para almacenar todos los alumnos
                for row in reader:  # recorre el archivo CSV fila por fila
                    fila = {}  # Genera un diccionario por cada registro en el csv
                    fila['matricula'] = row['matricula']  # obtiene la matricula y la agrega al diccionario
                    fila['nombre'] = row['nombre']  # optione el nombre y lo agrega al diccionario
                    fila['primer_apellido'] = row['primer_apellido']  # optiene el primer_apellido
                    fila['segundo_apellido'] = row['segundo_apellido']  # optiene el segundo apellido
                    fila['carrera'] = row['carrera']  # obtiene la carrera
                    alumnos.append(fila)  # agrega el diccionario generado al array alumnos
                result['alumnos'] = alumnos  # agrega el array alumnos al diccionario result
            return result  # Regresa el diccionario generado
        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado

    @staticmethod
    def actionSearch(app_version, file,matricula):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status

            with open(file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                alumnos = []
                for row in reader:
                    if(row['matricula'] == matricula):
                        alumnos.append(row)
                        result['alumnos'] = row
                        break #Permite cambiar el estado cuando la matricula no se encuentra
                    else:
                        result = {}
                        result['app_version'] = app_version
                        result['status'] = "Parameter Not Found"
            return result

        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado

    @staticmethod
    def actionPut(app_version, file, alumno):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"  # mensaje de status

            with open(file, 'a+', newline='') as csvfile:
                writer =csv.writer(csvfile) # csvfile es una variable_cualquiera
                writer.writerow(alumno)

            with open(file, 'r') as csvfile:
                reader = csv.DictReader(csvfile) # csvfile es una variable_cualquiera
                alumnos = []  # array para almacenar todos los alumnos
                for row in reader:  # recorre el archivo CSV fila por fila
                    fila = {}  # Genera un diccionario por cada registro en el csv
                    fila['matricula'] = row['matricula']  # obtiene la matricula y la agrega al diccionario
                    fila['nombre'] = row['nombre']  # optione el nombre y lo agrega al diccionario
                    fila['primer_apellido'] = row['primer_apellido']  # optiene el primer_apellido
                    fila['segundo_apellido'] = row['segundo_apellido']  # optiene el segundo apellido
                    fila['carrera'] = row['carrera']  # obtiene la carrera
                    alumnos.append(fila)  # agrega el diccionario generado al array alumnos
                result['alumnos'] = alumnos  # agrega el array alumnos al diccionario result
            return result  # Regresa el diccionario generado

        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado

    @staticmethod
    def actionDelete(app_version, file, matricula):
        try:
            result = {}  # crear diccionario vacio
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "200 ok"

            with open(file, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                alumnos = []
                for row in reader:
                    if (row['matricula'] != matricula):
                        alumnos.append(row)
                        result['alumnos'] = row
            tam = (len(alumnos))
            with open(file,'w',newline='') as csvfile:
                writer=csv.writer(csvfile)
                fila=[]
                fila.append("matricula")
                fila.append("nombre")
                fila.append("primer_apellido")
                fila.append("segundo_apellido")
                fila.append("carrera")
                writer.writerow(fila)
                data=[]
                for i in range(0,tam):
                    data.append(alumnos[i]['matricula'])
                    data.append(alumnos[i]['nombre'])
                    data.append(alumnos[i]['primer_apellido'])
                    data.append(alumnos[i]['segundo_apellido'])
                    data.append(alumnos[i]['carrera'])
                    writer.writerow(data)
                    data=[]

            with open(file,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    alumnos.append(row)
                    result['alumnos']=alumnos
            return result

        except Exception as e:
            result = {}  # crear diccionario vacio
            print("Error {}".format(e.args))
            result['app_version'] = app_version  # version de la webapp
            result['status'] = "Error "  # mensaje de status
            return result  # Regresa el diccionario generado