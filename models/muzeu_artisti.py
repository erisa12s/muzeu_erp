from odoo import models, fields

class MuzeuArtisti(models.Model):
    _name = 'muzeu.artisti'
    _description = 'Artisti i Muzeut'

    name = fields.Char(string='Emri', required=True)
    mbiemer = fields.Char(string='Mbiemri')
    kombesia = fields.Char(string='Kombësia')
    periudha = fields.Char(string='Periudha / Stili')
    data_lindjes = fields.Date(string='Data e Lindjes')
    data_vdekjes = fields.Date(string='Data e Vdekjes')
    foto = fields.Binary(string='Foto')
    biografia = fields.Text(string='Biografia')
    
    vepra_ids = fields.One2many('muzeu.vepra', 'artisti_id', string='Veprat e Artit')