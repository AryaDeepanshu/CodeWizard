import web
from web.db import register_database
from Models import RegisterModel, LoginModel

urls = (
    '/', 'Home',
    '/register','Register',
    '/postregistration', 'PostRegistration',
    '/login', 'Login',
    '/check-login', 'CheckLogin'

)
render = web.template.render('Viewes\Templates', base='MainLayout')
app = web.application(urls, globals())


class Home:
    def GET(self):
        return render.Home()

class Register:
    def GET(self):
        return render.Register()


class PostRegistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.username


class Login:
    def GET(self):
        return render.Login()


class CheckLogin:
    def POST(self):
        data = web.input()
        login = LoginModel.LoginModel()
        isCorrect =  login.check_user(data)
        if isCorrect:
            return isCorrect
        return "error"


if __name__ == "__main__":
    app.run()