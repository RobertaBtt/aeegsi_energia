# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

class TipoTensione(models.Model):

    _name = "aeegsi_energia.tipo_tensione"

    etichetta = fields.Char(string="Etichetta tensione", required=True)
    descrizione = fields.Char(string="Descrizione tensione", required=True)

    @api.one
    def name_get(self):
        return self.id, self.descrizione
