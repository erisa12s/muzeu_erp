from odoo import models, fields

class MuzeuArtisti(models.Model):
    _name = 'muzeu.artisti'
    _description = 'Artisti i Muzeut'

    name = fields.Char(string='Emri', required=True)
    mbiemer = fields.Char(string='Mbiemri', required=True)
    datelindja = fields.Date(string='Datëlindja')
    shtetesia = fields.Char(string='Shtetësia')
    biografia = fields.Text(string='Biografia')
    
    vepra_ids = fields.One2many('muzeu.vepra', 'artisti_id', string='Veprat e Artistit')