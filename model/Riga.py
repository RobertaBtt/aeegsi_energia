# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

OPERATORE = [
    ('<', '<'),
    ('<=', '<='),
    ('=', '='),
    ('>', '>'),
    ('>=', '>=')
]

class Riga(models.Model):

    _name = "aeegsi_energia.riga"

    descrizione = fields.Text(string="Descrizione Riga", required=True)

    tipo_uso_id = fields.Many2one('aeegsi_energia.tipo_uso', "Tipo Uso") #utenza
    tipo_tensione_id = fields.Many2one('aeegsi_energia.tipo_tensione', "Tipo Tensione") #tipo

    potenza_impegnata_limite_inferiore = fields.Char(string="Potenza impegnata limite inferiore (kW)", digits=(3, 2))
    potenza_impegnata_limite_superiore = fields.Char(string="Potenza impegnata limite superiore (kW)", digits=(3, 2))
    operatore_potenza_impegnata_limite_inferiore = fields.Selection(OPERATORE, string="é")
    operatore_potenza_impegnata_limite_superiore = fields.Selection(OPERATORE, string="é")

    potenza_disponibile_limite_inferiore = fields.Char(string="Potenza disponibile limite inferiore (kW)",digits=(3, 2))
    potenza_disponibile_limite_superiore = fields.Char(string="Potenza disponibile limite superiore (kW)", digits=(3, 2))
    operatore_potenza_disponibile_limite_inferiore = fields.Selection(OPERATORE, string="é")
    operatore_potenza_disponibile_limite_superiore = fields.Selection(OPERATORE, string="é")

    tensione_limite_inferiore = fields.Char(string="Tensione limite inferiore (kV)")
    tensione_limite_superiore = fields.Char(string="Tensione limite superiore (kV)")
    operatore_tensione_limite_inferiore = fields.Selection(OPERATORE, string="é")
    operatore_tensione_limite_superiore = fields.Selection(OPERATORE, string="é")

    consumo_annuo_limite_inferiore = fields.Char(string="Consumo annuo limite inferiore (kWh)")
    consumo_annuo_limite_superiore = fields.Char(string="Consumo annuo limite superiore (kWh)")
    operatore_consumo_annuo_limite_inferiore = fields.Selection(OPERATORE, string="é")
    operatore_consumo_annuo_limite_superiore = fields.Selection(OPERATORE, string="é")

    # corrispettivo_unitario = fields.Char(string="Corrispettivo unitario")
    # valore_generico = fields.Char(string="Valore generico")
    #
    # creata_il = fields.Date(string="Data creazione riga")
    # aggiornata_il = fields.Date(string="File modificato da AEEGSI il: ")
    # versione = fields.Char(string="Versione", required=True, default = "1")


    @api.one
    def name_get(self):
        return self.id, self.descrizione