from odoo import models, fields

class MuzeuItinerari(models.Model):
    _name = 'muzeu.itinerari'
    _description = 'Itineraret e Muzeut'

    name = fields.Char(string='Emri i Itinerarit', required=True)
    pershkrimi = fields.Text(string='Përshkrimi')
    kohezgjatja = fields.Float(string='Kohëzgjatja (orë)')
    cmimi_shtese = fields.Float(string='Çmimi Shtesë (€)', default=0.0)
    
    kati_ids = fields.Many2many('muzeu.kati', string='Katet e Përfshira')
    ciceron_id = fields.Many2one(
        'muzeu.stafi', 
        string='Guida/ Ciceroni',
        domain="[('pozicioni', '=', 'ciceron')]"
    )