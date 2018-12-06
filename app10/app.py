import web
        
urls = (
    '/', 'application.controllers.index.Index',
    '/acercade','application.controllers.acercade.Acercade',
    '/insert', 'application.controllers.insert.Insert',
    '/iniciarsesion', 'application.controllers.iniciarsesion.Iniciarsesion',
    '/admin', 'application.controllers.admin.Admin',
    '/update/(.*)', 'application.controllers.update.Update',
    '/delete/(.*)', 'application.controllers.delete.Delete',
    '/view/(.*)', 'application.controllers.view.View',
    '/registrarse', 'application.controllers.registrarse.Registrarse',
    '/recuperarcuenta', 'application.controllers.recuperarcuenta.Recuperarcuenta',
    '/borrar', 'application.controllers.borrar.Borrar',
    '/actualizar', 'application.controllers.actualizar.Actualizar',
    '/logo', 'application.controllers.logo.Logo',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
