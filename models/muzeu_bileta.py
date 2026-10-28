from odoo import models, fields, api

class MuzeuBileta(models.Model):
    _name = 'muzeu.bileta'
    _description = 'Biletat e Muzeut'
    _rec_name = 'code'

    def _get_next_ticket_code(self):
        last_ticket = self.search([('code', 'like', 'BIL-%')], order='id desc', limit=1)
        if last_ticket and last_ticket.code:
            try:
                last_number = int(last_ticket.code.split('-')[1])
                return f'BIL-{(last_number + 1):04d}'
            except (IndexError, ValueError):
                return 'BIL-0001'
        return 'BIL-0001'

    code = fields.Char(
        string='Kodi i Biletës', 
        required=True, 
        readonly=True, 
        default=_get_next_ticket_code,
        copy=False
    )
    
    vizitori_id = fields.Many2one('muzeu.vizitori', string='Vizitori', required=True, ondelete='cascade')
    emri_vizitorit = fields.Char(string='Emri i Vizitorit', related='vizitori_id.display_name', store=True, readonly=True)
    
    lloji_biletes_id = fields.Many2one('muzeu.lloji.biletes', string='Lloji i Biletës', required=True)
    
    # --- ITINERARI DHE Guida ---
    itinerari_id = fields.Many2one('muzeu.itinerari', string='Itinerari / Turi (Guide)')
    kati_ids = fields.Many2many('muzeu.kati', string='Akses në Kat', related='itinerari_id.kati_ids', readonly=True)
    stafi_id = fields.Many2one('muzeu.stafi', string='Guide / Ciceroni', related='itinerari_id.ciceron_id', readonly=True)
    
    # --- LLOGARITJA AUTOMATIKE E ÇMIMIT KOMBINIT (BILETË + ITINERAR) ---
    cmimi = fields.Float(string='Çmimi Total (€)', compute='_compute_cmimi', store=True, readonly=True)

    @api.depends('lloji_biletes_id.cmimi', 'itinerari_id.cmimi_shtese')
    def _compute_cmimi(self):
        for rec in self:
            cmimi_baze = rec.lloji_biletes_id.cmimi if rec.lloji_biletes_id else 0.0
            cmimi_gid = rec.itinerari_id.cmimi_shtese if rec.itinerari_id else 0.0
            rec.cmimi = cmimi_baze + cmimi_gid

    # Detajet e Pagesës
    menyra_pageses = fields.Selection([
        ('kesh', 'Kesh'),
        ('karte', 'Kartë Bankare'),
    ], string='Mënyra e Pagesës', default='kesh', required=True)
    
    valuta = fields.Selection([
        ('ALL', 'ALL (Lekë)'),
        ('EUR', 'EUR (€)'),
        ('USD', 'USD ($)')
    ], string='Valuta', default='ALL', required=True)

    data_blerjes = fields.Datetime(string='Data e Blerjes', default=fields.Datetime.now)
    
    state = fields.Selection([
        ('draft', 'E Papaguar'),
        ('paid', 'E Paguar / Valide'),
        ('cancel', 'Anuluar'),
    ], string='Statusi', default='draft')

    def action_paguaj(self):
        self.state = 'paid'

    def action_anullo(self):
        self.state = 'cancel'