import tornado.web
import tornado
from service.ProphetService import *
from service.ValidateService import *

class ForecastHandler(tornado.web.RequestHandler):
    
    def post(self):
        fileinfo = tornado.escape.json_decode(self.request.body.fileinfo)
        periods = tornado.escape.json_decode(self.request.body.periods)
        season_type = tornado.escape.json_decode(self.request.body.season_type)

        if not fileinfo:
            return getMessageFailFileinfo()

        if not periods:
            return getMessageFailPeriods()

        if not season_type:
            return getMessageFailSeasonType()

        result = continousForecast(fileinfo, periods, season_type)

        self.write('oi fiori')