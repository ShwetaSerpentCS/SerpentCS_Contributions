# See LICENSE file for full copyright and licensing details.

from odoo import models


class Crmleadextended(models.Model):
    _inherit = "crm.lead"

    def get_lead_stage_data(self):
        crm_lst = []
        for stage in self.env["crm.stage"].search([]):
            leads = self.search_count([("stage_id", "=", stage.id)])
            crm_lst.append((stage.name, int(leads)))
        return crm_lst
