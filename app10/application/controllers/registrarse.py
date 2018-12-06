import web

render= web .template.render('application/views/',base='master')


class Registrarse:
    def __init__(self):
        pass

    def GET(self):
        datos=['5513096571','30']
        return render.registrarse(datos)