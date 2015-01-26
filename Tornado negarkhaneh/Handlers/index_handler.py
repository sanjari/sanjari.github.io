import tornado
from models import negar
__author__ = 'mojtaba.banaie'


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        catInfo = negar.select()
        self.render('index.html', catInfo=catInfo)
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")
