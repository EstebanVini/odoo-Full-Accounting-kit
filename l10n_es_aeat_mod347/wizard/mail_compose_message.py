# Copyright 2023 FactorLibre - Alejandro Ji Cheung
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    def _action_send_mail(self, auto_commit=False):
        res = super()._action_send_mail(auto_commit=auto_commit)
        default_model = self._context.get("default_model", False)
        partner_record_model = "l10n.es.aeat.mod347.partner_record"
        if default_model == partner_record_model:
            active_id = self._context.get("active_id")
            record = self.env[partner_record_model].browse(active_id)
            record.write({"state": "sent"})
        return res
