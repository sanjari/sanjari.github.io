__author__ = 'mojtaba.banaie'
from Handlers.index_handler import IndexHandler
# from Handlers.category__handler import CategoryHandler,CategoryEditHandler,CategoryDeleteHandler,CategoryNewHandler
from Handlers.img_handier import negarEditHandler,negarDeleteHandler,negarNewHandler,ShowHandler,adminHandler

urlList = [
    (r'/', IndexHandler),
    # (r'/category$', CategoryHandler),
    (r'/negar/edit/(\d+)$', negarEditHandler),
    (r'/negar/delete/(\d+)$', negarDeleteHandler),
    (r'/negar/new$', negarNewHandler),
    (r'/negar/show$', ShowHandler),
    (r'/login$', adminHandler)

]