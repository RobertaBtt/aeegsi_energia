__author__ = 'roberta@enermed.it'

from openerp.addons.web.http import HttpRequest, Response
from openerp import models, fields, api
import simplejson

class AEEGSIRequest(HttpRequest):

    def __init__(self, *args):
        super(AEEGSIRequest, self).__init__(*args)
        self.params = self.httprequest.args.to_dict()
        self.headers = {
            'Access-Control-Max-Age': 60 * 60 * 24,
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
        }



    def dispatchRequest(self ):
        #checkParams
        response = self.params
        # response = {
        #     'jsonrpc': '2.0',
        #     'result': "postino"
        #     }

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                   ('Content-Length', len(body))])


