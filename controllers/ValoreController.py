# -*- coding: utf-8 -*-

from openerp.addons.web.http import Controller, route, HttpRequest, Response

from openerp.http  import request
from openerp import http
from openerp import models, fields, api, SUPERUSER_ID
import simplejson

#----------------------------------------------------------
# AEEGSI Web Controllers
#----------------------------------------------------------

class ValoreController(Controller):

    #Esempio: http://localhost:8069/aeegsi/valore/query?componente=UC3&tipo=variabile&uso=d&tensione=BT

    #TODO: non funziona esternamente neanche con auth = none o public.
    # non é possibile usare auth = none se si usa il database

    @http.route('/web/aeegsi/valore/query', type='http', auth="user")
    def getValore(self, **kw):


        #Esempio: http://localhost:8069/aeegsi/valore/query?componente=UC3&tipo=variabile&uso=d&tensione=BT

        searchDomainValore = []

        response = {}
        self.params = request.httprequest.args.to_dict()
        self.headers = {
            'Access-Control-Max-Age': 60 * 60 * 24,
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
        }


        valore_env = request.registry.get('aeegsi_energia.valore')
        if self.params.has_key('componente'):
            searchDomainValore.append(('tabella_id.componente_id.codice', '=', self.params['componente']))
        if self.params.has_key('tipo'):
            searchDomainValore.append(('tabella_id.componente_id.tipo_componente_id.tipo', '=', self.params['tipo']))
        if self.params.has_key('uso'):
            searchDomainValore.append(('riga_id.tipo_uso_id.etichetta', '=', self.params['uso']))
        if self.params.has_key('tensione'):
            searchDomainValore.append(('riga_id.tipo_tensione_id.etichetta', '=', self.params['tensione']))

        #valore_list = valore_env.search(request.cr, request.uid, searchDomainValore)
        if not request.session.uid:
            uid = SUPERUSER_ID
        else:
            uid = request.session.uid

        valore_list = valore_env.search(request.cr, uid, searchDomainValore)

        if len(valore_list) == 1:
            valoreId = valore_list[0]
            fields = ['valore']
            valore = valore_env.read(request.cr, uid, valoreId, fields)
            response = str(valore['valore'])
        elif len(valore_list)==0: response['errore'] = "Nessun valore"
        elif len(valore_list)>1: response['errore'] = "Più di un valore trovato"

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                       ('Content-Length', len(body))])


        return ""

    @http.route('/aeegsi/valore/get/tabella/<id_tabella>/riga/<id_riga>', type='http', auth="none")
    def valore_get(self, s_action=None, db=None, **kw):
        idTabella = idRiga = 0
        response = {}

        try:
            idTabella = int(kw['id_tabella'])
            idRiga = int(kw['id_riga'])
        except:
            response['errore'] = "Formato parametro errato"
            mime = 'application/json'
            body = simplejson.dumps(response)
            return Response(body, headers=[('Content-Type', mime), ('Content-Length', len(body))])


        valore_env = request.registry.get('aeegsi_energia.valore')
        valore = valore_env.search(request.cr, request.uid, [('riga_id', '=', idRiga), ('tabella_id', '=', idTabella)])

        if len(valore) == 1:

            valoreId = valore[0]
            fields = ['valore', 'tipo_valore_euro', 'unita_di_misura_id']

            valore = valore_env.read(request.cr, request.uid, valoreId, fields)
            response[valoreId] = str(valore['valore'])
        elif len(valore)==0: response['errore'] = "Nessun valore"
        elif len(valore)>1: response['errore'] = "Più di un valore trovato"

        mime = 'application/json'
        body = simplejson.dumps(response)

        return Response(body, headers=[('Content-Type', mime),
                                       ('Content-Length', len(body))])
