from odoo import models, fields

class MuzeuSalla(models.Model):
    _name = 'muzeu.salla'
    _description = 'Sallat e Muzeut'

    name = fields.Char(string='Emri i Sallës')
    nr = fields.Integer(string='Numri i Sallës', required=True)
    lloji = fields.Selection([
        ('ekspozite', 'Sallë Ekspozite'),
        ('magazine', 'Magazinë / Arkiv'),
        ('restaurim', 'Laborator Restaurimi')
    ], string='Lloji i Sallës', default='ekspozite')
    siperfaqe = fields.Float(string='Sipërfaqja (m²)')
    kapaciteti = fields.Integer(string='Kapaciteti Maksimal')
    
    kati_id = fields.Many2one('muzeu.kati', string='Kati', required=True, ondelete='cascade')

    def _compute_display_name(self):
        for rec in self:
            if rec.name:
                rec.display_name = f"Salla {rec.nr} - {rec.name}"
            else:
                rec.display_name = f"Salla {rec.nr}"