from odoo import models

from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    # es_pymes_canary chart
    @template("es_pymes_canary", "account.tax")
    def _get_es_pymes_canary_account_tax_reav(self):
        additional = self._parse_csv(
            "es_pymes_canary", "account.tax", module="l10n_es_igic_reav"
        )
        return additional

    @template("es_pymes_canary", "account.fiscal.position")
    def _get_es_pymes_canary_account_fiscal_position_reav(self):
        return self._parse_csv(
            "es_pymes_canary", "account.fiscal.position", module="l10n_es_igic_reav"
        )

    # es_full_canary chart
    @template("es_full_canary", "account.tax")
    def _get_es_full_canary_account_tax_reav(self):
        additional = self._parse_csv(
            "es_full_canary", "account.tax", module="l10n_es_igic_reav"
        )
        return additional

    @template("es_full_canary", "account.fiscal.position")
    def _get_es_full_canary_account_fiscal_position_reav(self):
        return self._parse_csv(
            "es_full_canary", "account.fiscal.position", module="l10n_es_igic_reav"
        )
