from odoo import models, fields

class MuzeuDemtimet(models.Model):
    _name = 'muzeu.demtimet'
    _description = 'Raportimi i Dëmtimeve dhe Mirëmbajtjes së Veprave'

    name = fields.Char(string='Titulli i Raportit', required=True)
    vepra_id = fields.Many2one('muzeu.vepra', string='Vepra e Artit', required=True, ondelete='cascade')
    data_raportimit = fields.Date(string='Data e Raportimit', default=fields.Date.today, required=True)
    
    shkalla_demit = fields.Selection([
        ('lehte', 'I Lehtë'),
        ('mesatare', 'I Mesëm'),
        ('rende', 'I Rëndë / Kritik'),
    ], string='Shkalla e Dëmit', default='lehte', required=True)
    
    state = fields.Selection([
        ('raportuar', 'I Raportuar'),
        ('ne_restaurim', 'Në Proces Restaurimi'),
        ('rregulluar', 'I Rregulluar / Përfunduar'),
    ], string='Statusi', default='raportuar', required=True)
    
    raportues_id = fields.Many2one('muzeu.stafi', string='Raportuar nga (Stafi)')
    pershkrimi = fields.Text(string='Përshkrimi i Dëmit / Detajet e Restaurimit')

    # VEPRIMET E STATUSIT (ACTION BUTTONS)
    def action_start_restoration(self):
        for rec in self:
            rec.state = 'ne_restaurim'
            # Kalojmë edhe vetë veprën në statusin 'ne_restaurim'
            if rec.vepra_id:
                rec.vepra_id.state = 'ne_restaurim'

    def action_finish_restoration(self):
        for rec in self:
            rec.state = 'rregulluar'
            # Rikthejmë veprën në statusin 'ekspozuar'
            if rec.vepra_id:
                rec.vepra_id.state = 'ekspozuar'

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = 'raportuar'