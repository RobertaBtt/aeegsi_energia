# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

class Colonna(models.Model):

    _name = "aeegsi_energia.colonna"

    descrizione = fields.Text(string="Descrizione Colonna", required = True)
    nome = fields.Char(string="Nome Colonna", required = True)

    _sql_constraints = [('descr_nome_unique', 'unique(descrizione, nome)', 'Descrizione e nome già inseriti')]

    # aggiornata_il = fields.Date(string="File modificato da AEEGSI il: ")
    # versione = fields.Char(string="Versione", required=True, default = "1")

    @api.one
    def name_get(self):
        return self.id, self.descrizione

