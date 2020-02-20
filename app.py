import web  # pip install web.py

urls = (  # Indica que son tuplas, que tienen dos valores
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',
    '/alumnos_json/?', 'application.controllers.alumnos_json.Alumnos',
    '/alumnos_inse/?', 'application.controllers.insertalum.Alumnos',
)
app = web.application(urls, globals())  # Configura como una aplicacion

# render = web.template.render('templates/')

if __name__ == "__main__":
    web.config.debug = False
    app.run()

# Para cambiar el puerto: 'python app.py 123(Numero de puerto a ejecutar)'
