import web

urls = (
    '/', 'home',
    "/register","register"
)
render = web.template.render('Viewes\Templates', base='MainLayout')
app = web.application(urls, globals())

class register:
    def GET(self):
        return render.Register()

class home:
    def GET(self):
        return render.Home()
if __name__ == "__main__":
    app.run()