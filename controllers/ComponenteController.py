
# -*- coding: utf-8 -*-

from openerp.addons.web.http import Controller, route, HttpRequest, Response
from openerp.http  import request
from . import AEEGSIRequest
import simplejson

#----------------------------------------------------------
# AEEGSI Web Controllers
#----------------------------------------------------------
class ComponenteController(Controller):


    @route('/aeegsi/componente/get/codice/<codice>', type='http', auth="user")
    def componente_get(self, s_action=None, db=None, **kw):
        paramId = str(kw['codice'])
        response = {}
        componente_env = request.registry.get('aeegsi_energia.componente')
        componente = componente_env.search(request.cr, request.uid, [('codice', '=', paramId)])
        if len(componente) == 1:

            componenteId = componente[0]

            fields = ['codice', 'descrizione']

            componente = componente_env.read(request.cr, request.uid, componenteId, fields)
            response[componenteId] = componente
        elif len(componente)==0: response['errore'] = "Nessun componente con codice " + paramId
        elif len(componente)>1: response['errore'] = "Più di un componente con codice " + paramId

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                   ('Content-Length', len(body))])

