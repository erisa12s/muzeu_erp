from odoo import models, fields, api

class MuzeuVepra(models.Model):
    _name = 'muzeu.vepra'
    _description = 'Vepra e Artit'

    name = fields.Char(string='Emri i Veprës', required=True)
    artisti_id = fields.Many2one('muzeu.artisti', string='Artisti')
    lloji = fields.Selection([
        ('pikture', 'Pikturë'),
        ('skulpture', 'Skulpturë'),
        ('mozaik', 'Mozaik'),
        ('fotografi', 'Fotografi'),
        ('artefakt', 'Artefakt Historik'),
    ], string='Lloji i Veprës', default='pikture')
    
    rryma = fields.Char(string='Rryma Artistike')
    viti_krijimit = fields.Integer(string='Viti i Krijimit')
    data_ekspozimit = fields.Date(string='Data e Ekspozimit')
    
    kati_id = fields.Many2one('muzeu.kati', string='Kati')
    salla_id = fields.Many2one('muzeu.salla', string='Salla')
    vlera = fields.Float(string='Vlera (€)')
    foto = fields.Binary(string='Foto e Veprës')
    pershkrim = fields.Text(string='Përshkrimi')
    
    state = fields.Selection([
        ('ekspozuar', 'Në Ekspozitë'),
        ('ne_ruajtje', 'Në Ruajtje / Depo'),
        ('ne_restaurim', 'Në Restaurim'),
    ], string='Statusi', default='ekspozuar')
    
    # Lidhja me Dëmtimet
    demtimet_ids = fields.One2many('muzeu.demtimet', 'vepra_id', string='Dëmtimet / Mirëmbajtja')
    demtimet_count = fields.Integer(string='Numri i Dëmtimeve', compute='_compute_demtimet_count')

    @api.depends('demtimet_ids')
    def _compute_demtimet_count(self):
        for rec in self:
            rec.demtimet_count = len(rec.demtimet_ids)

    def action_view_demtimet(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Dëmtimet e Veprës',
            'res_model': 'muzeu.demtimet',
            'view_mode': 'list,form',
            'domain': [('vepra_id', '=', self.id)],
            'context': {'default_vepra_id': self.id},
        }