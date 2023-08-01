# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

TIPO_FILE = [
    ('xls', 'Foglio di calcolo'),
    ('pdf', 'Portable Document Format (PDF)'),
    ('doc', 'Documento')
]

class Tabella(models.Model):

    _name = "aeegsi_energia.tabella"

    titolo = fields.Text(string="Titolo Tabella", required = True)
    nome_file = fields.Char(string="Nome del File", required = True)
    url_file = fields.Char(string="Url File", required=True)
    tipo_file = fields.Selection(TIPO_FILE, string="Tipo del file", required=True)
    componente_id = fields.Many2one('aeegsi_energia.componente', "Componente riferito", required=True)
    n_tab = fields.Integer(string="Numero di Tab nel Foglio di Calcolo")
    n_pag = fields.Integer(string="Numero di Pagina nel Documento")

    creata_il = fields.Date(string="Data creazione tabella")
    aggiornata_il = fields.Date(string="File modificato da AEEGSI il: ")
    versione = fields.Char(string="Versione", required=True, default = "1")

    @api.one
    def name_get(self):
        return self.id, self.titolo + "(" + self.nome_file+ ")"

