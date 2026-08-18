from odoo import models, fields

class MuzeuLlojiBiletes(models.Model):
    _name = 'muzeu.lloji.biletes'
    _description = 'Llojet e Biletave dhe Çmimet'

    name = fields.Char(string='Emri i Biletës', required=True)
    cmimi = fields.Float(string='Çmimi (€)', required=True)
    pershkrim = fields.Text(string='Përshkrimi')