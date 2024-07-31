from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def format_validity_date(self):
        self.ensure_one()
        if self.validity_date:
            return self.validity_date.strftime('%d.%m.%Y')
        return ''

    def get_formatted_date(self):
        self.ensure_one()
        month_names = {
            1: 'січня', 2: 'лютого', 3: 'березня', 4: 'квітня',
            5: 'травня', 6: 'червня', 7: 'липня', 8: 'серпня',
            9: 'вересня', 10: 'жовтня', 11: 'листопада', 12: 'грудня'
        }
        if self.date_order:
            day = self.date_order.day
            month = month_names.get(self.date_order.month)
            year = self.date_order.year
            return f'{day} {month} {year}'
        return ''
