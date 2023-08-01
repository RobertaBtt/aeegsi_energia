# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api


class Componente(models.Model):

    _name = "aeegsi_energia.componente"

    codice = fields.Char(string="Codice componente", required = True)
    descrizione = fields.Text(string="Descrizione componente", required = True)
    tipo_componente_id = fields.Many2one('aeegsi_energia.tipo_componente', "Tipo di Componente")

    _sql_constraints = [('cod_descr_tipo_unique', 'unique(codice, descrizione, tipo_componente_id)', 'Componente con codice, descrizione, tipo già esistente!')]

    @api.one
    def name_get(self):
        return self.id, self.codice + "(" + self.tipo_componente_id.tipo + ")"
