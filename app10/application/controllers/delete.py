import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Delete:
    def __init__(self):
        pass

    def GET(self, id): 
        datos = model_datos.select_email(id) 
        return render.delete(datos)
    
    def POST(self, id):
        formulario = web.input()
        id = formulario['id']
        model_datos.delete_datos(id)
        raise web.seeother('/borrar')
