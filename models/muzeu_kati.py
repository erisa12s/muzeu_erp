from odoo import models, fields

class MuzeuKati(models.Model):
    _name = 'muzeu.kati'
    _description = 'Katet e Muzeut'
    _rec_name = 'name'

    name = fields.Char(string='Emri i Katit', required=True)
    niveli = fields.Integer(string='Niveli (Kati)', default=0)
    nr_sallash = fields.Integer(string='Numri i Sallave')
    
    salla_ids = fields.One2many('muzeu.salla', 'kati_id', string='Sallat')