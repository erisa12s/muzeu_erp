from odoo import models, fields, api

class MuzeuVizitori(models.Model):
    _name = 'muzeu.vizitori'
    _description = 'Vizitori i Muzeut'
    _rec_name = 'display_name'

    emer = fields.Char(string='Emri', required=True)
    mbiemer = fields.Char(string='Mbiemri', required=True)
    display_name = fields.Char(string='Emri i Plotë', compute='_compute_display_name', store=True)
    
    tel = fields.Char(string='Telefon')
    email = fields.Char(string='Email')
    shtetesia = fields.Char(string='Shtetësia', default='Shqiptar')
    
    registation = fields.Selection([
        ('kasa', 'Në Arkë / Kasë'),
        ('web', 'web'),
        ('app', 'App'),
    ], string='Kanali i Regjistrimit', default='kasa', required=True)
    
    created_at = fields.Datetime(string='Data e Regjistrimit', default=fields.Datetime.now, readonly=True)
    
    # Relacioni One2many me biletat
    bileta_ids = fields.One2many('muzeu.bileta', 'vizitori_id', string='Biletat')
    
    # Statak e komputuara me 'paid' dhe 'used'
    nr_vizitave = fields.Integer(string='Numri i Vizitave', compute='_compute_statistikat', store=True)
    totali_shpenzuar = fields.Float(string='Totali i Shpenzuar', compute='_compute_statistikat', store=True)

    @api.depends('emer', 'mbiemer')
    def _compute_display_name(self):
        for rec in self:
            if rec.emer and rec.mbiemer:
                rec.display_name = f"{rec.emer} {rec.mbiemer}"
            else:
                rec.display_name = rec.emer or rec.mbiemer or "Vizitor Pa Emër"

    @api.depends('bileta_ids', 'bileta_ids.cmimi', 'bileta_ids.state')
    def _compute_statistikat(self):
        for rec in self:
            # Filtrojmë biletat që janë në statuset 'paid' ose 'used'
            biletat_paguara = rec.bileta_ids.filtered(lambda b: b.state in ['paid', 'used'])
            rec.nr_vizitave = len(biletat_paguara)
            rec.totali_shpenzuar = sum(biletat_paguara.mapped('cmimi'))

    def action_view_biletat(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': f'Biletat e {self.display_name}',
            'res_model': 'muzeu.bileta',
            'view_mode': 'list,form',
            'domain': [('vizitori_id', '=', self.id)],
            'context': {'default_vizitori_id': self.id},
        }