import web

render= web .template.render('application/views/',base='master')


class Iniciarsesion:
    def __init__(self):
        pass

    def GET(self):
        datos=['5513096571','30']
        return render.iniciarsesion(datos)