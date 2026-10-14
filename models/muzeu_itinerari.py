from odoo import models, fields, api

class MuzeuItinerari(models.Model):
    _name = 'muzeu.itinerari'
    _description = 'Itinerari'
    _rec_name = 'emri'

    emri = fields.Char(string='Emri i Itinerarit', required=True)
    kohezgjatja = fields.Float(string='Kohëzgjatja1', help=' 1.5 / 1 orë ')
    kapaciteti = fields.Integer(string='Kapaciteti Maksimal')
    nr_salla = fields.Integer(string='Numri i Sallave', compute='_compute_nr_salla', store=True)
    cmimi_baze = fields.Float(string='Çmimi Bazë (€)', required=True)
    cmimi_student = fields.Float(string='Çmimi për Studentë (€)')
    cmimi_femije = fields.Float(string='Çmimi për Fëmijë (€)')
    
    gjuha = fields.Selection([
        ('al', 'Shqip'),
        ('en', 'Anglisht'),
        ('it', 'Italisht'),
        ('fr', 'Frëngjisht'),
        ('de', 'Gjermanisht'),
    ], string='Gjuha e Turit', default='al', required=True)
    
    state = fields.Selection([
        ('draft', 'Ne Pergatitje'),
        ('aktiv', 'Aktiv'),
        ('paaktiv', 'Jo Aktiv'),
    ], string='Statusi', default='draft')

    stafi_id = fields.Many2one(
        'muzeu.stafi', 
        string='Ciceroni / Pergjegjesi',
        domain="[('pozicioni', '=', 'Ciceron')]" 
    )
    
    detaje_ids = fields.One2many(
        'muzeu.itinerari.detaje', 
        'itinerari_id', 
        string='Sallat e Itinerarit'
    )

    @api.depends('detaje_ids')
    def _compute_nr_salla(self):
        for rec in self:
            rec.nr_salla = len(rec.detaje_ids)


class MuzeuItinerariDetaje(models.Model):
    _name = 'muzeu.itinerari.detaje'
    _description = 'Detajet e Sallave në Itinerar'
    _order = 'radha asc '

    itinerari_id = fields.Many2one('muzeu.itinerari', string='Itinerari', ondelete='cascade')
    salla_id = fields.Many2one('muzeu.salla', string='Salla', required=True)
    radha = fields.Integer(string='Radha e Vizitës', default=1)
    kati_id = fields.Many2one(related='salla_id.kati_id', string='Kati', readonly=True)