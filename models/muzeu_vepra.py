from odoo import models, fields

class MuzeuVepra(models.Model):
    _name = 'muzeu.vepra'
    _description = 'Vepra e Artit / Eksponati'

    name = fields.Char(string='Emri i Veprës', required=True)
    data_krijimit = fields.Date(string='Data e Krijimit')
    data_ekspozimit = fields.Date(string='Data e Ekspozimit')
    rryma = fields.Char(string='Rryma Artistike')
    lloji = fields.Selection([
        ('pikture', 'Pikturë'),
        ('skulture', 'Skulpturë'),
        ('mozaik', 'Mozaik'),
        ('antikitete', 'Antikitet / Qeramikë'),
        ('tjerat', 'Tjetër'),
    ], string='Lloji i Veprës', default='pikture')
    pershkrim = fields.Text(string='Përshkrimi')
    foto = fields.Binary(string='Foto e Veprës')
    
    state = fields.Selection([
        ('ekspozuar', 'Në Ekspozitë'),
        ('depo', 'Në Depo'),
        ('restaurim', 'Në Restaurim'),
        ('huazuar', 'E Huazuar Jashtë'),
    ], string='Statusi', default='ekspozuar')

    salla_id = fields.Many2one('muzeu.salla', string='Salla ku Ekspozohet')
    artisti_id = fields.Many2one('muzeu.artisti', string='Artisti / Autori')