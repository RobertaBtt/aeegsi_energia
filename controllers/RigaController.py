# -*- coding: utf-8 -*-

from openerp.addons.web.http import Controller, route, HttpRequest, Response
from openerp.http  import request
from . import AEEGSIRequest
import simplejson

#----------------------------------------------------------
# AEEGSI Web Controllers
#----------------------------------------------------------
class RigaController(Controller):


    @route('/aeegsi/riga/list', type='http', auth="user")
    def tabella_list(self, s_action=None, db=None, **kw):

        #aeegsiRequest = AEEGSIRequest.AEEGSIRequest(request.httprequest)
        riga_env = request.registry.get('aeegsi_energia.riga')
        riga_ids = riga_env.search(request.cr, request.uid, [])
        response = {}


        fields =['descrizione', 'tipo_uso_id', 'tipo_tensione_id', \
                 'potenza_impegnata_limite_inferiore', 'potenza_impegnata_limite_superiore', \
                 'operatore_potenza_impegnata_limite_inferiore', 'operatore_potenza_impegnata_limite_superiore', \
                 ]
        for id in riga_ids:
            riga = riga_env.read(request.cr, request.uid, id, fields)
            response[id] = riga

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                   ('Content-Length', len(body))])

