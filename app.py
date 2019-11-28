import motor.motor_tornado

import tornado.ioloop
import tornado.web
import tornado.httpserver

from handlers.ForecastHandler import ForecastHandler

class Application(tornado.web.Application):
    def __init__(self):

        handlers = [
            (r"/forecast", ForecastHandler),
        ]

        tornado.web.Application.__init__(self, handlers)

if __name__ == "__main__":

    app = tornado.httpserver.HTTPServer(Application())
    app.listen(7777)

    print('Server running on port 7777')

    tornado.ioloop.IOLoop.current().start()