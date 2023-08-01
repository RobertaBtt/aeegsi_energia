# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

class TipoUso(models.Model):

    _name = "aeegsi_energia.tipo_uso"

    etichetta = fields.Char(string="Etichetta tipo d'uso", required=True)
    descrizione = fields.Char(string="Descrizione tipo d'uso", required=True)

    @api.one
    def name_get(self):
        return self.id, self.descrizione
