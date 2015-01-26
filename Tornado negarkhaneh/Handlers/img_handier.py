import tornado
from models import *
import peewee


__author__ = 'Javad'

class ShowHandler(tornado.web.RequestHandler):
    def get(self):
        catInfo = negar.select().order_by(negar.id.desc())
        self.render('show.html', catInfo=catInfo)

class negarEditHandler(tornado.web.RequestHandler):
     def get(self, *args):
       catId = args[0]
       catInfo = negar.select().where(negar.id == catId).get()
       self.render("edit.html", catInfo=catInfo)


     def post(self, *args):
       catId = args[0]
       catInfo = negar.select().where(negar.id == catId).get()

       img2 = self.get_argument("img")
       img3 = "../static/img/mahbob/%s" %(img2)
       catInfo.img = img3
       catInfo.save()


       self.redirect("/")



class negarDeleteHandler(tornado.web.RequestHandler):
     def get(self, *args):
       cat_id = args[0]
       nInfo = negar.select().where(negar.id == cat_id).get().delete_instance()
       self.redirect("/")



class negarNewHandler(tornado.web.RequestHandler):
     def get(self, *args):
       self.render("new.html")


     def post(self, *args):

       Name = self.get_argument("img")
       img2 = "../static/img/mahbob/%s" %(Name)
       nInfo = negar.create(
           img=img2
       )

       self.redirect("/")


class adminHandler(tornado.web.RequestHandler):
    def get(self):
        login1=login.select()
        self.render("login/index.html",login1=login1)