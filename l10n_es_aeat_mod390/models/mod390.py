# Copyright 2017-2021 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl

from odoo import _, api, exceptions, fields, models
from odoo.tools import float_compare

ACTIVITY_CODE_SELECTION = [
    (
        "1",
        "1: Actividades sujetas al Impuesto sobre Actividades Económicas "
        "(Activ. Empresariales)",
    ),
    (
        "2",
        "2: Actividades sujetas al Impuesto sobre Actividades Económicas "
        "(Activ. Profesionales y Artísticas)",
    ),
    ("3", "3: Arrendadores de Locales de Negocios y garajes"),
    ("4", "4: Actividades Agrícolas, Ganaderas o Pesqueras, no sujetas al IAE"),
    (
        "5",
        "5: Sujetos pasivos que no hayan iniciado la realización de entregas "
        "de bienes o prestaciones de servicios correspondientes a actividades "
        "empresariales o profesionales y no estén dados de alta en el IAE",
    ),
    ("6", "6: Otras actividades no sujetas al IAE"),
]
REPRESENTATIVE_HELP = _("Nombre y apellidos del representante")
NOTARY_CODE_HELP = _(
    "Código de la notaría en la que se concedió el poder de representación "
    "para esta persona."
)


class L10nEsAeatMod390Report(models.Model):
    _description = "AEAT 390 report"
    _inherit = "l10n.es.aeat.report.tax.mapping"
    _name = "l10n.es.aeat.mod390.report"
    _aeat_number = "390"
    _period_quarterly = False
    _period_monthly = False
    _period_yearly = True

    # 3. Datos estadísticos
    has_347 = fields.Boolean(
        string="¿Obligación del 347?",
        default=True,
        help="Marque la casilla si el sujeto pasivo ha efectuado con alguna "
        "persona o entidad operaciones por las que tenga obligación de "
        "presentar la declaración anual de operaciones con terceras "
        "personas (modelo 347).",
    )
    main_activity = fields.Char(string="Actividad principal", size=40)
    main_activity_code = fields.Selection(
        selection=ACTIVITY_CODE_SELECTION,
        string="Código actividad principal (antiguo)",
    )
    main_activity_code_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod303.report.activity.code",
        domain="["
        "   '|',"
        "   ('period_type', '=', False), ('period_type', '=', period_type),"
        "   '&',"
        "   '|', ('date_start', '=', False), ('date_start', '<=', date_start),"
        "   '|', ('date_end', '=', False), ('date_end', '>=', date_end),"
        "]",
        string="Código actividad principal",
    )
    main_activity_iae = fields.Char(
        string="Epígrafe I.A.E. actividad principal",
        size=4,
    )
    other_first_activity = fields.Char(string="1ª actividad", size=40)
    other_first_activity_code = fields.Selection(
        selection=ACTIVITY_CODE_SELECTION,
        string="Código 1ª actividad (antiguo)",
        readonly=True,
    )
    other_first_activity_code_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod303.report.activity.code",
        domain="["
        "   '|',"
        "   ('period_type', '=', False), ('period_type', '=', period_type),"
        "   '&',"
        "   '|', ('date_start', '=', False), ('date_start', '<=', date_start),"
        "   '|', ('date_end', '=', False), ('date_end', '>=', date_end),"
        "]",
        string="Código 1ª actividad",
    )
    other_first_activity_iae = fields.Char(
        string="Epígrafe I.A.E. 1ª actividad",
        size=4,
    )
    other_second_activity = fields.Char(string="2ª actividad", size=40)
    other_second_activity_code = fields.Selection(
        selection=ACTIVITY_CODE_SELECTION,
        string="Código 2ª actividad (antiguo)",
    )
    other_second_activity_code_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod303.report.activity.code",
        domain="["
        "   '|',"
        "   ('period_type', '=', False), ('period_type', '=', period_type),"
        "   '&',"
        "   '|', ('date_start', '=', False), ('date_start', '<=', date_start),"
        "   '|', ('date_end', '=', False), ('date_end', '>=', date_end),"
        "]",
        string="Código 2ª actividad",
    )
    other_second_activity_iae = fields.Char(
        string="Epígrafe I.A.E. 2ª actividad",
        size=4,
    )
    other_third_activity = fields.Char(string="3ª actividad", size=40)
    other_third_activity_code = fields.Selection(
        selection=ACTIVITY_CODE_SELECTION,
        string="Código 3ª actividad (antiguo)",
    )
    other_third_activity_code_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod303.report.activity.code",
        domain="["
        "   '|',"
        "   ('period_type', '=', False), ('period_type', '=', period_type),"
        "   '&',"
        "   '|', ('date_start', '=', False), ('date_start', '<=', date_start),"
        "   '|', ('date_end', '=', False), ('date_end', '>=', date_end),"
        "]",
        string="Código 3ª actividad",
    )
    other_third_activity_iae = fields.Char(
        string="Epígrafe I.A.E. 3ª actividad",
        size=4,
    )
    other_fourth_activity = fields.Char(string="4ª actividad", size=40)
    other_fourth_activity_code = fields.Selection(
        selection=ACTIVITY_CODE_SELECTION,
        string="Código 4ª actividad (antiguo)",
    )
    other_fourth_activity_code_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod303.report.activity.code",
        domain="["
        "   '|',"
        "   ('period_type', '=', False), ('period_type', '=', period_type),"
        "   '&',"
        "   '|', ('date_start', '=', False), ('date_start', '<=', date_start),"
        "   '|', ('date_end', '=', False), ('date_end', '>=', date_end),"
        "]",
        string="Código 4ª actividad",
    )
    other_fourth_activity_iae = fields.Char(
        string="Epígrafe I.A.E. 4ª actividad",
        size=4,
    )
    other_fifth_activity = fields.Char(string="5ª actividad", size=40)
    other_fifth_activity_code = fields.Selection(
        selection=ACTIVITY_CODE_SELECTION,
        string="Código 5ª actividad (antiguo)",
    )
    other_fifth_activity_code_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod303.report.activity.code",
        domain="["
        "   '|',"
        "   ('period_type', '=', False), ('period_type', '=', period_type),"
        "   '&',"
        "   '|', ('date_start', '=', False), ('date_start', '<=', date_start),"
        "   '|', ('date_end', '=', False), ('date_end', '>=', date_end),"
        "]",
        string="Código 5ª actividad",
    )
    other_fifth_activity_iae = fields.Char(
        string="Epígrafe I.A.E. 5ª actividad",
        size=4,
    )
    # 4. Representantes
    first_representative_name = fields.Char(
        string="Nombre del primer representante",
        size=80,
        help=REPRESENTATIVE_HELP,
    )
    first_representative_vat = fields.Char(
        string="NIF del primer representante",
        size=9,
    )
    first_representative_date = fields.Date(
        string="Fecha poder del primer representante",
    )
    first_representative_notary = fields.Char(
        string="Notaría del primer representante",
        size=12,
        help=NOTARY_CODE_HELP,
    )
    second_representative_name = fields.Char(
        string="Nombre del segundo representante",
        size=80,
        help=REPRESENTATIVE_HELP,
    )
    second_representative_vat = fields.Char(
        string="NIF del segundo representante",
        size=9,
    )
    second_representative_date = fields.Date(
        string="Fecha poder del segundo representante",
    )
    second_representative_notary = fields.Char(
        string="Notaría del segundo representante",
        size=12,
        help=NOTARY_CODE_HELP,
    )
    third_representative_name = fields.Char(
        string="Nombre del tercer representante",
        size=80,
        help=REPRESENTATIVE_HELP,
    )
    third_representative_vat = fields.Char(
        string="NIF del tercer representante",
        size=9,
    )
    third_representative_date = fields.Date(
        string="Fecha poder del tercer representante",
    )
    third_representative_notary = fields.Char(
        string="Notaría del tercer representante",
        size=12,
        help=NOTARY_CODE_HELP,
    )
    # 5. Régimen general
    casilla_33 = fields.Monetary(
        compute="_compute_casilla_33",
        string="[33] Total bases IVA",
        store=True,
    )
    casilla_34 = fields.Monetary(
        compute="_compute_casilla_34",
        string="[34] Total cuotas IVA",
        store=True,
    )
    casilla_47 = fields.Monetary(
        compute="_compute_casilla_47",
        store=True,
        string="[47] Total cuotas IVA y recargo de equivalencia",
    )
    casilla_48 = fields.Monetary(
        compute="_compute_casilla_48",
        store=True,
        string="[48] Total base deducible operaciones corrientes",
    )
    casilla_49 = fields.Monetary(
        compute="_compute_casilla_49",
        store=True,
        string="[49] Total cuota deducible operaciones corrientes",
    )
    casilla_50 = fields.Monetary(
        compute="_compute_casilla_50",
        store=True,
        string="[50] Total bases imponibles deducibles en operaciones "
        "interiores de bienes de inversión",
    )
    casilla_51 = fields.Monetary(
        compute="_compute_casilla_51",
        store=True,
        string="[51] Total de cuotas deducibles en operaciones interiores de "
        "bienes de inversión",
    )
    casilla_52 = fields.Monetary(
        compute="_compute_casilla_52",
        store=True,
        string="[52] Total base deducible importaciones corrientes",
    )
    casilla_53 = fields.Monetary(
        compute="_compute_casilla_53",
        store=True,
        string="[53] Total cuota deducible importaciones corrientes",
    )
    casilla_54 = fields.Monetary(
        compute="_compute_casilla_54",
        store=True,
        string="[54] Total base deducible importaciones bienes de inversión",
    )
    casilla_55 = fields.Monetary(
        compute="_compute_casilla_55",
        store=True,
        string="[55] Total cuota deducible importaciones bienes de inversión",
    )
    casilla_56 = fields.Monetary(
        compute="_compute_casilla_56",
        store=True,
        string="[56] Total base deducible adq. intracomunitarias bienes",
    )
    casilla_57 = fields.Monetary(
        compute="_compute_casilla_57",
        store=True,
        string="[57] Total cuota deducible adq. intracomunitarias bienes",
    )
    casilla_58 = fields.Monetary(
        compute="_compute_casilla_58",
        store=True,
        string="[58] Total base deducible adq. intracomunitarias bienes de "
        "inversión",
    )
    casilla_59 = fields.Monetary(
        compute="_compute_casilla_59",
        store=True,
        string="[59] Total cuota deducible adq. intracomunitarias bienes de "
        "inversión",
    )
    casilla_597 = fields.Monetary(
        compute="_compute_casilla_597",
        store=True,
        string="[597] Total base deducible adq. intracomunitarias servicios",
    )
    casilla_598 = fields.Monetary(
        compute="_compute_casilla_598",
        store=True,
        string="[598] Total cuota deducible adq. intracomunitarias servicios",
    )
    casilla_64 = fields.Monetary(
        compute="_compute_casilla_64",
        store=True,
        string="[64] Suma de deducciones",
    )
    casilla_65 = fields.Monetary(
        compute="_compute_casilla_65",
        store=True,
        string="[65] Result. rég. gral.",
    )
    casilla_658 = fields.Monetary(
        string="[658] Regularización cuotas art. 80. Cinco.5ª LIVA",
    )
    casilla_662 = fields.Monetary(
        string="[662] Cuotas pendientes de compensación al término del ejercicio",
        help="[662] Cuotas pendientes de compensación generadas en el ejercicio "
        "y distintas de las incluidas en la casilla 97",
    )
    casilla_84 = fields.Monetary(
        compute="_compute_casilla_84",
        store=True,
        string="[84] Suma de resultados",
    )
    casilla_85 = fields.Monetary(
        string="[85] Compens. ejercicio anterior",
        help="Se consignará el importe de las cuotas pendientes de compensación "
        "generadas en ejercicios anteriores y aplicadas en el ejercicio (es "
        "decir, que se hubiesen consignado en la casilla 78 de alguna de las "
        "autoliquidaciones del periodo).",
    )
    casilla_86 = fields.Monetary(
        compute="_compute_casilla_86",
        store=True,
        string="[86] Result. liquidación",
    )
    # 9. Resultado de las liquidaciones
    casilla_95 = fields.Monetary(
        string="[95] Total resultados a ingresar modelo 303",
        help="Se consignará la suma de las cantidades a ingresar por el "
        "Impuesto como resultado de las autoliquidaciones periódicas "
        "del ejercicio que no tributen en el régimen especial del grupo "
        "de entidades, incluyendo aquellas para las que se hubiese "
        "solicitado aplazamiento, fraccionamiento o no se hubiese "
        "efectuado el pago.",
    )
    casilla_97 = fields.Monetary(
        string="[97] Result. 303 último periodo a compensar",
        help="Si el resultado de la última autoliquidación fue a compensar, "
        "consignará en esta casilla el importe de la misma.",
    )
    casilla_98 = fields.Monetary(
        string="[98] Result. 303 último periodo a devolver",
        help="Si el resultado de la última autoliquidación fue a devolver, "
        "consignará en esta casilla el importe de la misma.",
    )
    casilla_108 = fields.Monetary(
        string="[108] Total vol. oper.",
        compute="_compute_casilla_108",
        store=True,
    )
    use_303 = fields.Boolean(
        "Use 303 reports",
        help="If it's checked, this report uses 303 reports for calculate fields 85, "
        "95, 97, 98 and 662. When it's unchecked, you should fill them in. If you "
        "calculated first and then checked this option, you must calculate it again.",
        default=False,
    )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_33(self):
        for report in self:
            report.casilla_33 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number
                    in (
                        700,
                        667,
                        1,
                        702,
                        669,
                        3,
                        5,  # Régimen ordinario
                        704,
                        671,
                        500,
                        706,
                        673,
                        502,
                        504,  # Intragrupo - no incluido aún
                        708,
                        675,
                        643,
                        710,
                        677,
                        645,
                        647,  # Criterio de caja - no incluido aún
                        712,
                        679,
                        7,
                        714,
                        681,
                        9,
                        11,  # Bienes usados, etc - no incluido aún
                        13,  # Agencias de viajes - no incluido aún
                        716,
                        683,
                        21,
                        718,
                        685,
                        23,
                        25,  # Adquis. intracomunitaria bienes
                        720,
                        687,
                        545,
                        722,
                        689,
                        547,
                        551,  # Adquis. intracomunitaria servicios
                        27,  # IVA otras operaciones sujeto pasivo
                        29,  # Modificación bases y cuotas
                        649,  # Modif. bases y cuotas intragrupo - no incluido aún
                        31,  # Modif. bases y cuotas concurso ac. - no incluido aún
                    )
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_34(self):
        for report in self:
            report.casilla_34 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number
                    in (
                        701,
                        668,
                        2,
                        703,
                        670,
                        4,
                        6,  # Régimen ordinario
                        705,
                        672,
                        501,
                        707,
                        674,
                        503,
                        505,  # Intragrupo - no incluido aún
                        709,
                        676,
                        644,
                        711,
                        678,
                        46,
                        648,  # Criterio de caja - no incluido aún
                        713,
                        680,
                        8,
                        715,
                        682,
                        10,
                        12,  # Bienes usados, etc - no incluido aún
                        14,  # Agencias de viajes - no incluido aún
                        717,
                        684,
                        22,
                        719,
                        686,
                        24,
                        26,  # Adquis. intracomunitaria bienes
                        721,
                        688,
                        546,
                        723,
                        690,
                        548,
                        552,  # Adquis. intracomunitaria servicios
                        28,  # IVA otras operaciones sujeto pasivo
                        30,  # Modificación bases y cuotas
                        650,  # Modif. bases y cuotas intragrupo - no incluido aún
                        32,  # Modif. bases y cuotas concurso ac. - no incluido aún
                    )
                ).mapped("amount")
            )

    @api.depends("casilla_34", "tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_47(self):
        for report in self:
            report.casilla_47 = report.casilla_34 + sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number
                    in (
                        664,
                        692,
                        36,
                        666,
                        694,
                        600,
                        602,
                        42,  # Recargo de equivalencia
                        44,  # Modificación recargo de equivalencia
                        46,  # Mod. recargo equiv. concurso - no incluido aún
                    )
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_38(self):
        """Deprecated field left for old reports. To be removed in newer versions."""
        for report in self:
            report.casilla_38 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (190, 192, 555, 603, 194, 557, 605)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_39(self):
        """Deprecated field left for old reports. To be removed in newer versions."""
        for report in self:
            report.casilla_39 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (191, 193, 556, 604, 195, 558, 606)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_48(self):
        for report in self:
            report.casilla_48 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (695, 190, 724, 697, 603, 605)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_49(self):
        for report in self:
            report.casilla_49 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (696, 191, 725, 698, 604, 606)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_50(self):
        for report in self:
            report.casilla_50 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (749, 196, 728, 751, 611, 613)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_51(self):
        for report in self:
            report.casilla_51 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (750, 197, 729, 752, 612, 614)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_52(self):
        for report in self:
            report.casilla_52 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (757, 202, 732, 759, 619, 621)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_53(self):
        for report in self:
            report.casilla_53 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (758, 203, 733, 760, 620, 622)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_54(self):
        for report in self:
            report.casilla_54 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (761, 208, 734, 763, 623, 625)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_55(self):
        for report in self:
            report.casilla_55 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (762, 209, 735, 764, 624, 626)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_56(self):
        for report in self:
            report.casilla_56 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (765, 214, 736, 767, 627, 629)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_57(self):
        for report in self:
            report.casilla_57 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (766, 215, 737, 768, 628, 630)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_58(self):
        for report in self:
            report.casilla_58 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (769, 220, 738, 771, 631, 633)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_59(self):
        for report in self:
            report.casilla_59 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (770, 221, 739, 772, 632, 634)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_597(self):
        for report in self:
            report.casilla_597 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (773, 587, 740, 775, 635, 637)
                ).mapped("amount")
            )

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_598(self):
        for report in self:
            report.casilla_598 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (774, 588, 741, 776, 636, 638)
                ).mapped("amount")
            )

    @api.depends(
        "casilla_49",
        "casilla_51",
        "casilla_53",
        "casilla_55",
        "casilla_57",
        "casilla_59",
        "casilla_598",
        "tax_line_ids",
        "tax_line_ids.amount",
    )
    def _compute_casilla_64(self):
        for report in self:
            report.casilla_64 = (
                report.casilla_49
                + report.casilla_51
                + report.casilla_53
                + report.casilla_55
                + report.casilla_57
                + report.casilla_59
                + report.casilla_598
                + sum(
                    report.tax_line_ids.filtered(
                        lambda x: x.field_number in (61, 62)
                    ).mapped("amount")
                )
            )

    @api.depends("casilla_47", "casilla_64")
    def _compute_casilla_65(self):
        for report in self:
            report.casilla_65 = report.casilla_47 - report.casilla_64

    @api.depends("casilla_65", "casilla_658")
    def _compute_casilla_84(self):
        for report in self:
            report.casilla_84 = report.casilla_65 + report.casilla_658

    @api.depends("casilla_84", "casilla_85")
    def _compute_casilla_86(self):
        for report in self:
            report.casilla_86 = report.casilla_84 - report.casilla_85

    @api.depends("tax_line_ids", "tax_line_ids.amount")
    def _compute_casilla_108(self):
        for report in self:
            report.casilla_108 = sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number
                    in (
                        99,
                        653,
                        103,
                        104,
                        105,
                        110,
                        100,
                        101,
                        102,
                        125,
                        126,
                        127,
                        128,
                        227,
                        228,
                    )
                ).mapped("amount")
            ) - sum(
                report.tax_line_ids.filtered(
                    lambda x: x.field_number in (106, 107)
                ).mapped("amount")
            )

    @api.constrains("statement_type")
    def _check_type(self):
        if "C" in self.mapped("statement_type"):
            raise exceptions.UserError(
                _("You cannot make complementary reports for this model.")
            )

    def _calculate_casilla_85(self, reports_303_this_year):
        self.ensure_one()
        report_303_first_period = reports_303_this_year.filtered(
            lambda r: r.period_type in {"1T", "1"}
        )
        # Si no hay autoliquidaciones del primer periodo del ejercicio, asumimos
        # que el total viene de ejercicios anteriores
        if not report_303_first_period:
            return sum(reports_303_this_year.mapped("cuota_compensar"))
        # Obtenemos cuotas pendientes de compensación generadas en ejercicios anteriores
        # Casilla [110] de la primera autoliquidación del ejercicio
        remaining_cuota_compensar = report_303_first_period.potential_cuota_compensar
        # Obtenemos total a compensar aplicado en el ejercicio
        # Casilla [78] de todas las autoliquidaciones del ejercicio (suma)
        total_cuota_compensar = sum(reports_303_this_year.mapped("cuota_compensar"))
        # Si durante el ejercicio se ha aplicado más de remaining_cuota_compensar,
        # entonces hemos aplicado el total durante el ejercicio.
        # En caso contrario, solo hemos aplicado una parte de
        # remaining_cuota_compensar, usamos la suma de las casillas [78]
        return min(total_cuota_compensar, remaining_cuota_compensar)

    def calculate(self):
        res = super().calculate()
        for mod390 in self:
            if not mod390.use_303:
                continue
            casilla_85, casilla_95, casilla_97, casilla_98, casilla_662 = 0, 0, 0, 0, 0
            reports_303_this_year = self.env["l10n.es.aeat.mod303.report"].search(
                [
                    ("year", "=", mod390.year),
                    ("state", "not in", ("draft", "cancelled")),
                    ("statement_type", "=", "N"),
                ]
            )
            if not reports_303_this_year:
                continue
            # casilla 85 = cuotas pendientes de compensación generadas en ejercicios
            # anteriores y aplicadas en el ejercicio
            casilla_85 = self._calculate_casilla_85(reports_303_this_year)
            # casilla 95 = sumatorio de las casilla 71 de los periodos del año que
            # sean a ingresar
            casilla_95 = sum(
                reports_303_this_year.filtered(
                    lambda r: r.result_type in {"I", "G", "U"}
                ).mapped("resultado_liquidacion")
            )
            report_303_last_period = reports_303_this_year.filtered(
                lambda r: r.period_type in {"4T", "12"}
            )
            if report_303_last_period:
                if report_303_last_period[0].result_type == "C":
                    # Si salió a compensar, casilla 97 = casilla 71 del último periodo
                    # del año si fue a compensar
                    casilla_97 = abs(report_303_last_period.resultado_liquidacion)
                else:
                    # casilla 662 = casilla 87 del último periodo del año si no se
                    # incluyo en la casilla 97
                    casilla_662 = report_303_last_period.remaining_cuota_compensar
                    if report_303_last_period[0].result_type in {"D", "V", "X"}:
                        # Si salió a devolver, casilla 98 = casilla 71 del último
                        #  periodo del año si fue a devolver
                        casilla_98 = abs(report_303_last_period.resultado_liquidacion)
            mod390.update(
                {
                    "casilla_85": casilla_85,
                    "casilla_95": casilla_95,
                    "casilla_97": casilla_97,
                    "casilla_98": casilla_98,
                    "casilla_662": casilla_662,
                }
            )
        return res

    def button_confirm(self):
        """Check that the manual 303 results match the report."""
        self.ensure_one()
        summary = self.casilla_95 - self.casilla_97 - self.casilla_98 - self.casilla_662
        if float_compare(summary, self.casilla_86, precision_digits=2) != 0:
            raise exceptions.UserError(
                _(
                    "The result of the manual 303 summary (fields [95], [97], [98] and "
                    "[662] in the page '9. Resultado liquidaciones') doesn't match "
                    "the field [86]. Please check if you have filled such fields."
                )
            )
        return super().button_confirm()

    def _get_move_line_domain(self, date_start, date_end, map_line):
        """Consider Bankrupcy proceedings or uncollectible debt."""
        res = super()._get_move_line_domain(date_start, date_end, map_line)
        if map_line.field_number in {31, 32}:
            res += [("move_id.is_bankrupcy_uncollectible_debt", "=", True)]
        elif map_line.field_number in {29, 30, 99}:
            res += [("move_id.is_bankrupcy_uncollectible_debt", "=", False)]
        return res
