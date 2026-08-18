from odoo import models, fields

class MuzeuBileta(models.Model):
    _name = 'muzeu.bileta'
    _description = 'Biletat e Muzeut'

    code = fields.Char(
        string='Kodi i Biletës', 
        required=True, 
        readonly=True, 
        default='E-TICKET'
    )
    emri_vizitorit = fields.Char(string='Emri i Vizitorit')
    
    # Relacioni dinamik me modelin e çmimeve (krijuar nga Menaxheri)
    lloji_biletes_id = fields.Many2one(
        'muzeu.lloji.biletes', 
        string='Lloji i Biletës', 
        required=True
    )
    
    # Çmimi merret automatikisht nga lloji i biletës së zgjedhur dhe nuk mund të ndryshohet nga kasieri
    cmimi = fields.Float(
        string='Çmimi (€)', 
        related='lloji_biletes_id.cmimi', 
        store=True, 
        readonly=True
    )
    
    data_blerjes = fields.Datetime(
        string='Data e Blerjes', 
        default=fields.Datetime.now
    )
    
    # Relacionet me Stafin dhe Katet
    stafi_id = fields.Many2one('muzeu.stafi', string='Lëshuar nga (Kasieri/Stafi)')
    kati_id = fields.Many2one('muzeu.kati', string='Akses në Kat')
    
    state = fields.Selection([
        ('draft', 'E Papaguar'),
        ('paid', 'E Paguar / Valide'),
        ('used', 'E Përdorur'),
        ('cancel', 'Anuluar'),
    ], string='Statusi', default='paid')