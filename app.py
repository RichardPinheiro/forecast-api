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

    tornado.httpserver.HTTPServer(Application())
    app.listen(9600)

    print('Server running on port 9600')

    tornado.ioloop.IOLoop.current().start()