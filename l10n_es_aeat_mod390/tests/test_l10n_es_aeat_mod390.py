# Copyright 2018-2021 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl

from collections import OrderedDict

from odoo import exceptions

from odoo.addons.l10n_es_aeat.tests.test_l10n_es_aeat_mod_base import (
    TestL10nEsAeatModBase,
)


class TestL10nEsAeatMod390Base(TestL10nEsAeatModBase):
    taxes_sale = {
        # tax code: (base, tax_amount)
        "S_IVA4B": (1000, 40),
        "S_IVA4B//neg": (-100, -4),
        "S_IVA4S": (1100, 44),
        "S_IVA10B": (1200, 120),
        "S_IVA10B//neg": (-120, -12),
        "S_IVA10S": (1300, 130),
        "S_IVA21B": (1400, 294),
        "S_IVA21B//neg": (-140, -29.4),
        "S_IVA21S": (1500, 315),
        "S_REQ05": (1700, 8.5),
        "S_REQ014": (1800, 25.2),
        "S_REQ52": (1900, 98.8),
        "S_IVA0_E": (2000, 0),
        "S_IVA_E": (2100, 0),
        "S_IVA_NS": (2200, 0),
        "S_IVA0_ISP": (2300, 0),
        "S_IVA0_IC": (2400, 0),
        "S_IVA0_SP_I": (2500, 0),
        "S_IVA0": (2600, 0),
    }
    taxes_purchase = {
        # tax code: (base, tax_amount)
        "P_IVA4_IC_BC": (100, 0),
        "P_IVA10_IC_BC": (200, 0),
        "P_IVA21_IC_BC": (300, 0),
        "P_IVA4_SP_IN": (400, 0),
        "P_IVA10_SP_IN": (500, 0),
        "P_IVA21_SP_IN": (600, 0),
        "P_IVA4_IC_BI": (700, 0),
        "P_IVA10_IC_BI": (800, 0),
        "P_IVA21_IC_BI": (900, 0),
        "P_IVA4_SP_EX": (110, 0),
        "P_IVA10_SP_EX": (120, 0),
        "P_IVA21_SP_EX": (130, 0),
        "P_IVA4_ISP": (140, 0),
        "P_IVA10_ISP": (150, 0),
        "P_IVA4_SC": (210, 8.4),
        "P_IVA10_SC": (220, 22),
        "P_IVA21_SC": (230, 48.3),
        "P_IVA4_BC": (240, 9.6),
        "P_IVA10_BC": (250, 25),
        "P_IVA21_BC": (260, 54.6),
        "P_REQ05": (270, 1.35),
        "P_REQ014": (280, 3.92),
        "P_REQ52": (290, 15.08),
        "P_IVA4_BI": (310, 12.4),
        "P_IVA10_BI": (320, 32),
        "P_IVA21_BI": (330, 69.3),
        "P_IVA4_IBC": (340, 13.6),
        "P_IVA10_IBC": (350, 35),
        "P_IVA21_IBC": (360, 75.6),
        "P_IVA4_IBI": (370, 14.8),
        "P_IVA10_IBI": (380, 38),
        "P_IVA21_IBI": (390, 81.9),
        "P_IVA0_BC": (400, 0),
        # "P_IVA12_AGR": (410, 49.2),
        "P_IVA0_ND": (420, 0),
    }
    taxes_result = OrderedDict(
        [
            # Régimen ordinario - Base imponible 4%
            ("1", 6000.0),
            # Régimen ordinario - Cuota 4%
            ("2", 240.0),
            # Régimen ordinario - Base imponible 10%
            ("3", 7140.0),
            # Régimen ordinario - Cuota 10%
            ("4", 714.0),
            # Régimen ordinario - Base imponible 21%
            ("5", 8280.0),
            # Régimen ordinario - Cuota 21%
            ("6", 1738.8),
            # Adquisiciones intracomunitarias de bienes - Base 4%
            ("21", 300.0),
            # Adquisiciones intracomunitarias de bienes - Cuota 4%
            ("22", 12.0),
            # Adquisiciones intracomunitarias de bienes - Base 10%
            ("23", 600.0),
            # Adquisiciones intracomunitarias de bienes - Cuota 10%
            ("24", 60.0),
            # Adquisiciones intracomunitarias de bienes - Base 21%
            ("25", 900.0),
            # Adquisiciones intracomunitarias de bienes - Cuota 21%
            ("26", 189.0),
            # IVA devengado otros supuestos de inversión del sujeto pasivo - Base
            ("27", 1950.0),  # (110 + 120 + 130 + 140 + 150) * 3
            # IVA devengado otros supuestos de inversión del sujeto pasivo - Cuota
            ("28", 192.9),  # (4.4 + 12 + 27,3 + 5.6 + 15) * 3
            # Modificación de bases
            ("29", -12290),  # -7140.0 - 4860.0 - 290.0
            # Modificación de cuotas
            ("30", -897.6 - 640.3),
            # Recargo de equivalencia - Base 0,5%
            ("35", 5100.0),
            # Recargo de equivalencia - Cuota 0,5%
            ("36", 25.5),
            # Modificación recargo equivalencia - Base
            ("43", -5400.0),
            # Modificación recargo equivalencia - Cuota
            ("44", -132.5),
            # Rectificación de deducciones - Cuota
            ("62", -1201.15),
            # Volumen de operaciones
            ("99", 14280.0),
            # Operaciones realizadas por sujetos pasivos acogidos al régimen
            # especial del recargo de equivalencia
            ("102", 0.0),
            # Entregas intracomunitarias exentas
            ("103", 9800.0),
            # Exportaciones y otras operaciones exentas con derecho a deducción
            ("104", 4000.0),
            # Operaciones exentas sin derecho a deducción
            ("105", 5200),
            # Adquisiciones intracomunitarias exentas
            ("109", 0.0),
            # Exportaciones y otras operaciones exentas con derecho a deducción
            ("110", 8600.0),  # (2*2100 + 2*2200) (S_IVA_E + S_IVA_NS)
            # IVA deducible en oper. corrientes de bienes y servicios - Base 4%
            ("190", 2100.0),
            # IVA deducible en oper. corrientes de bienes y servicios - Cuota 4%
            ("191", 84),
            # IVA deducible en oper. interiores de bienes de inversión - Base 4%
            ("196", 930),
            # IVA deducible en importaciones de bienes corrientes - Base 4%
            ("202", 1020.0),
            # IVA deducible en importaciones de bienes corrientes - Cuota 4%
            ("203", 40.8),
            # IVA deducible en adquisiciones intracom. bienes corrientes - Base 4%
            ("214", 300.0),
            # IVA deducible en adquisiciones intracomu. bienes corrientes -Cuota 4%
            ("215", 12.0),
            # Adquisiciones interiores exentas
            ("230", 800),
            # Importaciones exentas
            ("231", 0.0),
            # Bases imponibles del IVA soportado no deducible
            ("232", 840),
            # Adquisiciones intracomunitarias de servicios - Base 4%
            ("545", 1200.0),
            # Adquisiciones intracomunitarias de servicios - Cuota 4%
            ("546", 48.0),
            # Adquisiciones intracomunitarias de servicios - Base 10%
            ("547", 1500.0),
            # Adquisiciones intracomunitarias de servicios - Cuota 10%
            ("548", 150.0),
            # Adquisiciones intracomunitarias de servicios - Base 21%
            ("551", 1800.0),
            # Adquisiciones intracomunitarias de servicios - Cuota 21%
            ("552", 378.0),
            # IVA deducible en adquisiciones intracom. de servicios - Base 4%
            ("587", 1200.0),
            # IVA deducible en adquisiciones intracomu. de servicios - Cuota 4%
            ("588", 48.0),
            # Recargo de equivalencia - Base 1,4%
            ("599", 5400.0),
            # Recargo de equivalencia - Cuota 1,4%
            ("600", 75.6),
            # Recargo de equivalencia - Base 5,2%
            ("601", 5700.0),
            # Recargo de equivalencia - Cuota 5,2%
            ("602", 296.4),
            # IVA deducible operaciones corrientes bienes y servicios - Base 10%
            ("603", 2220),
            # IVA deducible operaciones corrientes bienes y servicios - Cuota 10%
            ("604", 222.0),
            # IVA deducible operaciones corrientes bienes y servicios - Base 21%
            ("605", 1860.0),  # (230 + 130 + 260) * 3
            # IVA deducible operaciones corrientes bienes y servicios - Cuota 21%
            ("606", 390.6),  # 1860 * 0.21
            # IVA deducible en importaciones de bienes corrientes - Base 10%
            ("619", 1050.0),
            # IVA deducible en importaciones de bienes corrientes - Cuota 10%
            ("620", 105.0),
            # IVA deducible en importaciones de bienes corrientes - Base 21%
            ("621", 1080.0),
            # IVA deducible en importaciones de bienes corrientes - Cuota 21%
            ("622", 226.8),
            # IVA deducible adquisiciones intracom. bienes corrientes - Base 10%
            ("627", 600.0),
            # IVA deducible adquisiciones intracom. bienes corrientes - Cuota 10%
            ("628", 60.0),
            # IVA deducible adquisiciones intracom. bienes corrientes - Base 21%
            ("629", 900.0),
            # IVA deducible adquisiciones intracom. bienes corrientes - Cuota 21%
            ("630", 189.0),
            # IVA deducible adquisiciones intracomunitarias servicios - Base 10%
            ("635", 1500.0),
            # IVA deducible adquisiciones intracomunitarias servicios - Cuota 10%
            ("636", 150.0),
            # IVA deducible adquisiciones intracomunitarias servicios - Base 21%
            ("637", 1800.0),
            # IVA deducible adquisiciones intracomunitarias servicios - Cuota 21%
            ("638", 378.0),
            # Rectificación de deducciones - Base
            ("639", -10550.0),
        ]
    )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create model
        cls.model390 = cls.env["l10n.es.aeat.mod390.report"].create(
            {
                "name": "9990000000390",
                "company_id": cls.company.id,
                "company_vat": "1234567890",
                "contact_name": "Test owner",
                "statement_type": "N",
                "support_type": "T",
                "contact_phone": "911234455",
                "year": 2017,
                "period_type": "0A",
                "date_start": "2017-01-01",
                "date_end": "2017-12-31",
                "journal_id": cls.journal_misc.id,
            }
        )
        cls.model390_2023 = cls.env["l10n.es.aeat.mod390.report"].create(
            {
                "name": "999000001390",
                "company_id": cls.company.id,
                "company_vat": "1234567890",
                "contact_name": "Test owner",
                "statement_type": "N",
                "support_type": "T",
                "contact_phone": "911234455",
                "year": 2023,
                "period_type": "0A",
                "date_start": "2023-01-01",
                "date_end": "2023-12-31",
                "journal_id": cls.journal_misc.id,
                "use_303": True,
            }
        )


class TestL10nEsAeatMod390(TestL10nEsAeatMod390Base):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Purchase invoices
        cls._invoice_purchase_create("2017-01-01")
        cls._invoice_purchase_create("2017-10-01")
        purchase = cls._invoice_purchase_create("2017-03-03")
        cls._invoice_refund(purchase, "2017-07-18")
        # Sale invoices
        cls._invoice_sale_create("2017-02-11")
        cls._invoice_sale_create("2017-06-12")
        sale = cls._invoice_sale_create("2017-11-13")
        cls._invoice_refund(sale, "2017-12-14")

    def test_model_390(self):
        # Test constraints
        with self.assertRaises(Exception) as ex:
            self.model390.statement_type = "C"
        self.model390.button_calculate()
        # Check tax lines
        for field, result in self.taxes_result.items():
            lines = self.model390.tax_line_ids.filtered(
                lambda x, field=field: x.field_number == int(field)
            )
            self.assertAlmostEqual(
                sum(lines.mapped("amount")),
                result,
                2,
                f"Incorrect result in field {field} {ex.exception}",
            )
        # Check computed fields
        self.assertAlmostEqual(self.model390.casilla_33, 17380.0, 2)
        self.assertAlmostEqual(self.model390.casilla_34, 2184.8, 2)
        self.assertAlmostEqual(self.model390.casilla_47, 2449.8, 2)
        self.assertAlmostEqual(self.model390.casilla_48, 6180.0, 2)
        self.assertAlmostEqual(self.model390.casilla_49, 696.6, 2)
        self.assertAlmostEqual(self.model390.casilla_50, 2880.0, 2)
        self.assertAlmostEqual(self.model390.casilla_51, 341.1, 2)
        self.assertAlmostEqual(self.model390.casilla_52, 3150.0, 2)
        self.assertAlmostEqual(self.model390.casilla_53, 372.6, 2)
        self.assertAlmostEqual(self.model390.casilla_54, 3420.0, 2)
        self.assertAlmostEqual(self.model390.casilla_55, 404.1, 2)
        self.assertAlmostEqual(self.model390.casilla_56, 1800.0, 2)
        self.assertAlmostEqual(self.model390.casilla_57, 261.0, 2)
        self.assertAlmostEqual(self.model390.casilla_58, 7200.0, 2)
        self.assertAlmostEqual(self.model390.casilla_59, 891.0, 2)
        self.assertAlmostEqual(self.model390.casilla_597, 4500.0, 2)
        self.assertAlmostEqual(self.model390.casilla_598, 576.0, 2)
        self.assertAlmostEqual(self.model390.casilla_64, 2341.25, 2)
        self.assertAlmostEqual(self.model390.casilla_65, 108.55, 2)
        self.assertAlmostEqual(self.model390.casilla_86, 108.55, 2)
        self.assertAlmostEqual(self.model390.casilla_108, 41880.0, 2)
        # It's not possible to confirm without entering manual 303 summary
        with self.assertRaises(exceptions.UserError):
            self.model390.button_confirm()
        self.model390.casilla_95 = 108.55
        self.model390.button_confirm()
        # Export to BOE
        export_to_boe = self.env["l10n.es.aeat.report.export_to_boe"].create(
            {"name": "test_export_to_boe.txt"}
        )
        export_config_xml_ids = [
            "l10n_es_aeat_mod390.aeat_mod390_2023_main_export_config",
            "l10n_es_aeat_mod390.aeat_mod390_2024_main_export_config",
        ]
        for xml_id in export_config_xml_ids:
            export_config = self.env.ref(xml_id)
            self.assertTrue(export_to_boe._export_config(self.model390, export_config))

    def test_model_390_using_303_01(self):
        # Check use 303 activated but no 303 reports exist
        # Purchase invoices
        self._invoice_purchase_create("2023-01-01")
        self._invoice_purchase_create("2023-04-01")
        self._invoice_purchase_create("2023-07-01")
        self._invoice_purchase_create("2023-10-01")
        # Sale invoices
        self._invoice_sale_create("2023-01-01")
        self._invoice_sale_create("2023-07-01")
        self._invoice_sale_create("2023-10-01")
        # Calculate 390
        self.model390_2023.button_calculate()
        self.assertAlmostEqual(self.model390_2023.casilla_85, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 0.0, 2)

    def test_model_390_using_303_02(self):
        # Check use 303 activated and 303 reports exist but none are to be enter
        # and last period is to return with remaining compensation
        # Purchase invoices
        self._invoice_purchase_create("2023-01-01")
        self._invoice_purchase_create("2023-10-01")
        # Reports 303
        model303_1T = self.env["l10n.es.aeat.mod303.report"].create(
            {
                "name": "9991000000303",
                "company_id": self.company.id,
                "company_vat": "1234567890",
                "contact_name": "Test owner",
                "statement_type": "N",
                "support_type": "T",
                "contact_phone": "911234455",
                "year": 2023,
                "period_type": "1T",
                "date_start": "2023-01-01",
                "date_end": "2023-03-31",
                "journal_id": self.journal_misc.id,
            }
        )
        model303_2T = model303_1T.copy(
            {
                "name": "9992000000303",
                "period_type": "2T",
                "date_start": "2023-04-01",
                "date_end": "2023-06-30",
            }
        )
        model303_3T = model303_1T.copy(
            {
                "name": "9993000000303",
                "period_type": "3T",
                "date_start": "2023-07-01",
                "date_end": "2023-09-30",
            }
        )
        model303_4T = model303_1T.copy(
            {
                "name": "9994000000303",
                "period_type": "4T",
                "date_start": "2023-10-01",
                "date_end": "2023-12-31",
            }
        )
        # Calculate reports
        model303_1T.button_calculate()
        model303_2T.button_calculate()
        model303_3T.button_calculate()
        model303_4T.button_calculate()
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 560.85, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 0.0, 2)

        model303_4T.return_last_period = True
        model303_4T.button_calculate()
        model303_4T.potential_cuota_compensar = 560.85
        model303_4T.cuota_compensar = 560.85
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 1121.7, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 0.0, 2)

        model303_1T.potential_cuota_compensar = 500.0
        model303_1T.button_calculate()
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 500.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 1121.7, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 0.0, 2)

        model303_1T.potential_cuota_compensar = 1000.0
        model303_1T.button_calculate()
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 560.85, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 1121.7, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 0.0, 2)

    def test_model_390_using_303_03(self):
        # Check use 303 activated, 303 reports exist and last period is to compensate
        # Purchase invoices
        self._invoice_purchase_create("2023-01-01")
        self._invoice_purchase_create("2023-04-01")
        self._invoice_purchase_create("2023-07-01")
        self._invoice_purchase_create("2023-10-01")
        # # Sale invoices
        self._invoice_sale_create("2023-01-01")
        self._invoice_sale_create("2023-04-01")
        self._invoice_sale_create("2023-07-01")
        self._invoice_sale_create("2023-10-01")
        # Reports 303
        model303_1T = self.env["l10n.es.aeat.mod303.report"].create(
            {
                "name": "9991000000303",
                "company_id": self.company.id,
                "company_vat": "1234567890",
                "contact_name": "Test owner",
                "statement_type": "N",
                "support_type": "T",
                "contact_phone": "911234455",
                "year": 2023,
                "period_type": "1T",
                "date_start": "2023-01-01",
                "date_end": "2023-03-31",
                "journal_id": self.journal_misc.id,
            }
        )
        model303_2T = model303_1T.copy(
            {
                "name": "9992000000303",
                "period_type": "2T",
                "date_start": "2023-04-01",
                "date_end": "2023-06-30",
            }
        )
        model303_3T = model303_1T.copy(
            {
                "name": "9993000000303",
                "period_type": "3T",
                "date_start": "2023-07-01",
                "date_end": "2023-09-30",
            }
        )

        model303_4T = model303_1T.copy(
            {
                "name": "9994000000303",
                "period_type": "4T",
                "date_start": "2023-10-01",
                "date_end": "2023-12-31",
            }
        )
        # Calculate reports
        model303_1T.button_calculate()
        model303_2T.button_calculate()
        model303_3T.button_calculate()
        model303_4T.potential_cuota_compensar = 905.25
        model303_4T.cuota_compensar = 805.25
        model303_4T.button_calculate()
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 1407.75, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 436.0, 2)

        model303_1T.potential_cuota_compensar = 2000.0
        model303_1T.button_calculate()
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 938.5, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 938.5, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 436.0, 2)

        model303_4T.return_last_period = True
        model303_4T.button_calculate()
        self.model390_2023.button_calculate()
        # Check casilla_85, casilla_95, casilla_97, casilla_98, casilla_662
        self.assertAlmostEqual(self.model390_2023.casilla_85, 1374.5, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_95, 938.5, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_97, 0.0, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_98, 436.00, 2)
        self.assertAlmostEqual(self.model390_2023.casilla_662, 0.0, 2)
