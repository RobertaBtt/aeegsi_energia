# -*- coding: utf-8 -*-
__author__ = 'roberta@enermed.it'


from openerp import models, fields, api

TIPO_VALORE_EURO = [
    ('1', 'Euro'),
    ('100', 'Centesimi di euro'),
    ('1000', 'Millesimi di euro')
]

class Valore(models.Model):

    _name = "aeegsi_energia.valore"

    descrizione = fields.Text(string="Descrizione Valore", required = True)
    tabella_id = fields.Many2one('aeegsi_energia.tabella', "Tabella")
    riga_id = fields.Many2one('aeegsi_energia.riga', "Riga")
    colonna_id = fields.Many2one('aeegsi_energia.colonna', "Colonna")
    regola_colonna_id = fields.Many2one('aeegsi_energia.regola_colonna', "Regola colonna")
    valore = fields.Float(string="Valore", required=True, default=0.0, digits=(6,7))
    tipo_valore_euro = fields.Selection(TIPO_VALORE_EURO, string="Tipo valore euro", required=True)
    unita_di_misura_id = fields.Many2one('aeegsi_energia.tipo_unita_misura', "Unita di misura")
    data_inizio_validita = fields.Date(string="Data inizio validita", required = True)
    data_fine_validita = fields.Date(string="Data fine validita", required = True)

    creata_il = fields.Date(string="Data creazione Valore", required=True)

    _order = 'creata_il desc'


    @api.one
    def name_get(self):
        return self.id, self.descrizione + "(File: "+self.tabella_id.nome_file+") Valore: "+str(self.valore)




