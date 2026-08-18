from odoo import models, fields

class MuzeuSalla(models.Model):
    _name = 'muzeu.salla'
    _description = 'Sallat e Muzeut'

    nr = fields.Integer(string='Numri i Sallës', required=True)
    lloji = fields.Selection([
        ('ekspozite', 'Sallë Ekspozite'),
        ('magazine', 'Magazinë / Arkiv'),
        ('restaurim', 'Laborator Restaurimi')
    ], string='Lloji i Sallës', default='ekspozite')
    siperfaqe = fields.Float(string='Sipërfaqja (m²)')
    kapaciteti = fields.Integer(string='Kapaciteti Maksimal')
    
    # Ky është Relacioni 1:N (Foreign Key për te Kati)
    kati_id = fields.Many2one('muzeu.kati', string='Kati', required=True, ondelete='cascade')