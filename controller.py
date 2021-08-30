import web
from web.db import register_database
from Models import RegisterModel, LoginModel, Posts

web.config.debug = False
urls = (
    '/', 'Home',
    '/register','Register',
    '/postregistration', 'PostRegistration',
    '/login', 'Login',
    '/check-login', 'CheckLogin',
    '/logout', 'Logout',
    '/post-activity', 'PostActivity'

)

app = web.application(urls, globals())
session = web.session.Session(app,web.session.DiskStore("session"), initializer={"user": None})
session_data = session._initializer
render = web.template.render('Viewes\Templates', base='MainLayout', globals={"session": session_data, "current_user": session_data["user"]})


class Home:
    def GET(self):
        post_model = Posts.Posts()
        posts = post_model.get_all_post()
        return render.Home(posts)
        

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
            session_data["user"] = isCorrect
            return isCorrect
        return "error"


class Logout:
    def GET(self):
        session["user"] = None
        session_data["user"] = None
        # session.kill()
        return "success"


class PostActivity:
    def POST(self):
        data = web.input()
        data.username = session_data['user']['username']
        post_model = Posts.Posts()
        post_model.insert_post(data)
        return "success"

if __name__ == "__main__":
    app.run()