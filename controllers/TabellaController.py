# -*- coding: utf-8 -*-

from openerp.addons.web.http import Controller, route, HttpRequest, Response
from openerp.http  import request
from . import AEEGSIRequest
import simplejson

#----------------------------------------------------------
# AEEGSI Web Controllers
#----------------------------------------------------------
class TabellaController(Controller):

    # a test
    @route('/aeegsi', type='http', auth="user")
    def aeegsi(self, s_action=None, db=None, **kw):

        #requestAeegsi = HttpRequest(request.httprequest)
        self.params = request.httprequest.args.to_dict()
        self.headers = {
            'Access-Control-Max-Age': 60 * 60 * 24,
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
        }

        response = self.params

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                   ('Content-Length', len(body))])


        # aeegsiRequest = AEEGSIRequest.AEEGSIRequest(request.httprequest)
        # return aeegsiRequest.dispatchRequest()

    @route('/aeegsi/tabella/list', type='http', auth="user")
    def tabella_list(self, s_action=None, db=None, **kw):

        #aeegsiRequest = AEEGSIRequest.AEEGSIRequest(request.httprequest)
        tabella_env = request.registry.get('aeegsi_energia.tabella')
        tabella_ids = tabella_env.search(request.cr, request.uid, [])
        response = {}
        fields =['nome_file', 'componente_id', 'n_pag', 'n_tab', 'display_name', 'titolo', 'url_file', 'tipo_file', 'versione', 'aggiornata_il']
        for id in tabella_ids:
            tabella = tabella_env.read(request.cr, request.uid, id, fields)
            response[id] = tabella

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                   ('Content-Length', len(body))])


    @route('/aeegsi/tabella/get/<id>', type='http', auth="user")
    def tabella_get(self, s_action=None, db=None, **kw):
        response = {}
        paramId = 0
        try:
            paramId = int(kw ['id'])
        except:
            response['errore'] = "Formato parametro errato"
            mime = 'application/json'
            body = simplejson.dumps(response)
            return Response(body, headers=[('Content-Type', mime), ('Content-Length', len(body))])

        tabella_env = request.registry.get('aeegsi_energia.tabella')

        fields =['nome_file', 'componente_id', 'n_pag', 'n_tab', 'display_name', 'titolo', 'url_file', 'tipo_file', 'versione', 'aggiornata_il']

        tabella = tabella_env.read(request.cr, request.uid, paramId, fields)
        response = tabella

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                   ('Content-Length', len(body))])

