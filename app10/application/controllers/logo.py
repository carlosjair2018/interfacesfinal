import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Logo:
    def __init__(self):
        pass

    def GET(self):  
        datos = model_datos.select_datos().list()
        return render.logo(datos)
