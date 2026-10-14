from odoo import models, fields

class MuzeuBileta(models.Model):
    _name = 'muzeu.bileta'
    _description = 'Biletat e Muzeut'
    _rec_name = 'code'  # Përdorim kodin ose emrin e vizitorit për shfaqje

    code = fields.Char(
        string='Kodi i Biletës', 
        required=True, 
        readonly=True, 
        default='E-TICKET'
    )
    
    # 1. Relacioni i ri me modelin e Vizitorit
    vizitori_id = fields.Many2one(
        'muzeu.vizitori', 
        string='Vizitori', 
        ondelete='cascade'
    )
    
    # Mund ta mbash si fushë 'related' me vizitorin për lehtësi
    emri_vizitorit = fields.Char(
        string='Emri i Vizitorit', 
        related='vizitori_id.display_name', 
        store=True, 
        readonly=True
    )
    
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