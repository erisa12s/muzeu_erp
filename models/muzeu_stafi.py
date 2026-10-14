from odoo import models, fields

class MuzeuStafi(models.Model):
    _name = 'muzeu.stafi'
    _description = 'Stafi i Muzeut'

    name = fields.Char(string='Emri', required=True)
    mbiemer = fields.Char(string='Mbiemri', required=True)
    email = fields.Char(string='Email')
    tel = fields.Char(string='Telefon')
    pozicioni = fields.Selection([
        ('menaxher', 'Menaxher Muzeu'),
        ('kurator', 'Kurator Arti'),
        ('ciceron', 'Ciceron / Ciceronë'),
        ('mbrojtje', 'Rojë Sigurie'),
        ('recepsionist', 'Recepsionist / Recepsioniste'),
        ('mirembajtje', 'Mirëmbajtës / Pastrues'),
    ], string='Pozicioni', default='ciceron', required=True)
    paga = fields.Float(string='Paga (€)')
    turni = fields.Selection([
        ('1', 'Turni I (Mëngjes)'),
        ('2', 'Turni II (Pasdite)'),
        ('3', 'Turni III (Natë)'),
    ], string='Turni', default='1')
    data_punesimit = fields.Date(string='Data e Punësimit')
    state = fields.Selection([
        ('aktiv', 'Aktiv'),
        ('pushim', 'Në Pushim'),
        ('larguar', 'I Larguar'),
    ], string='Statusi', default='aktiv')

    kati_id = fields.Many2one('muzeu.kati', string='Kati ku është caktuar')