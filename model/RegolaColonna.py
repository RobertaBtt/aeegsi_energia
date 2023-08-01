# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

class RegolaColonna(models.Model):

    _name = "aeegsi_energia.regola_colonna"

    descrizione = fields.Text(string="Descrizione Regola", required=True)
    valore_minimo = fields.Char(string="Valore minimo")
    valore_massimo = fields.Char(string="Valore massimo")
    valore_corrente = fields.Char(string="Valore corrente")
    creata_il = fields.Date(string="Data creazione Regola colonna")

    # aggiornata_il = fields.Date(string="File modificato da AEEGSI il: ")
    # versione = fields.Char(string="Versione", required=True, default = "1")

    @api.one
    def name_get(self):

        return self.id, self.descrizione
