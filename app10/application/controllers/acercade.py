import web

render= web .template.render('application/views/',base='master')


class Acercade:
    def __init__(self):
        pass

    def GET(self):
        datos=['5513096571','30']
        return render.acercade(datos)