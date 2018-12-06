import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Update:
    def __init__(self):
        pass

    def GET(self, id): 
        datos = model_datos.select_email(id) 
        return render.update(datos)
    
    def POST(self, id):
        formulario = web.input()
        id = formulario['id']
        nombre = formulario['nombre']
        precio = formulario['precio']
        existencia = formulario['existencia']
        model_datos.update_datos(id,nombre,precio,existencia)
        raise web.seeother('/actualizar')
