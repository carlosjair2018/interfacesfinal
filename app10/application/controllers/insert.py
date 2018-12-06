import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master2')

class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return render.insert()
    
    def POST(self):
        formulario = web.input()
        id = formulario['id']
        nombre = formulario['nombre']
        precio = formulario['precio']
        existencia = formulario['existencia']
        model_datos.insert_datos(id, nombre,precio,existencia)
        raise web.seeother('/admin')
