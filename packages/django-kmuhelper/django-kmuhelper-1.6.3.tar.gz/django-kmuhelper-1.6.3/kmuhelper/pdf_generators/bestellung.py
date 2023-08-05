"""PDF creator for invoices and delivery notes"""

from kmuhelper import settings
from kmuhelper.translations import autotranslate_mengenbezeichnung, autotranslate_kosten_name, langselect
from kmuhelper.utils import formatprice
from kmuhelper.pdf_generators._base import PDFGenerator

from reportlab.platypus import Table, TableStyle, Paragraph, Spacer, TopPadder, Flowable
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import black
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode import qr
from reportlab.graphics import renderPDF

from django.utils import translation
_ = translation.gettext


#####


class _PDFOrderPriceTable(Table):
    COLWIDTHS = [26*mm, 80*mm, 20*mm, 20*mm, 20*mm, 20*mm]

    @classmethod
    def from_bestellung(cls, bestellung):
        sprache = bestellung.kunde.sprache if bestellung.kunde else "de"

        data = [(_("Art-Nr."), _("Bezeichnung"), _("Anzahl"),
                 _("Einheit"), _("Preis"), _("Total"))]

        # Produkte

        h_produkte = 0

        for bp in bestellung.produkte.through.objects.filter(bestellung=bestellung):
            zwsumohnerabatt = bp.zwischensumme_ohne_rabatt()
            data.append((
                bp.produkt.artikelnummer,
                Paragraph(langselect(bp.produkt.name, sprache)),
                str(bp.menge),
                langselect(autotranslate_mengenbezeichnung(bp.produkt.mengenbezeichnung), sprache),
                formatprice(bp.produktpreis),
                formatprice(zwsumohnerabatt)
            ))
            h_produkte += 1
            if bp.rabatt:
                data.append((
                    "",
                    "- "+_("Rabatt"),
                    str(bp.rabatt),
                    "%",
                    formatprice(zwsumohnerabatt),
                    formatprice(bp.nur_rabatt())
                ))
                h_produkte += 1
            if bp.bemerkung:
                data.append((
                    "",
                    Paragraph(f"- <b>{bp.bemerkung}</b>"),
                    "",
                    "",
                    "",
                    ""
                ))
                h_produkte += 1

        # Kosten

        h_kosten = 0

        for bk in bestellung.kosten.through.objects.filter(bestellung=bestellung):
            data.append((
                "",
                Paragraph(langselect(autotranslate_kosten_name(bk.name), sprache)),
                "",
                "",
                "",
                formatprice(bk.preis)
            ))
            h_kosten += 1
            if bk.rabatt:
                data.append((
                    "",
                    "- "+_("Rabatt"),
                    str(bk.rabatt),
                    "%",
                    formatprice(bk.zwischensumme_ohne_rabatt()),
                    formatprice(bk.nur_rabatt())
                ))
                h_kosten += 1
            if bk.bemerkung:
                data.append((
                    "",
                    Paragraph(f"- <b>{bk.bemerkung}</b>"),
                    "",
                    "",
                    "",
                    ""
                ))
                h_kosten += 1

        # Mehrwertsteuer

        h_mwst = 0

        mwstdict = dict(bestellung.mwstdict())
        for mwstsatz in mwstdict:  # Mehrwertsteuer
            data.append((
                "",
                _("MwSt"),
                mwstsatz,
                "%",
                formatprice(float(mwstdict[mwstsatz])),
                formatprice(float(mwstdict[mwstsatz]*(float(mwstsatz)/100)))
            ))
            h_mwst += 1

        # Total & Zahlungskonditionen

        showpaycond = settings.get_db_setting(
            "print-payment-conditions", False)

        if showpaycond:
            payconds = bestellung.get_paymentconditions()
            totaltext = _("Rechnungsbetrag, zahlbar netto innert %s Tagen") % payconds[-1]["days"]
        else:
            totaltext = _("RECHNUNGSBETRAG")

        data.append((
            Paragraph(f"<b>{totaltext}</b>"),
            "",
            "",
            "CHF",
            "",
            formatprice(bestellung.fix_summe),
        ))

        h_paycond = 0
        if showpaycond:
            for paycond in payconds:
                if paycond["percent"] != 0.0:
                    data.append((
                        _("%(days)s Tage %(percent)s%% Skonto") % {"days": paycond["days"],
                                                                  "percent": paycond["percent"]},
                        "",
                        "",
                        "CHF",
                        "",
                        formatprice(paycond["price"]),
                    ))
                    h_paycond += 1

        # Style

        style = [
            # Horizontal lines
            # Header
            ('LINEABOVE', (0, 0), (-1, 0), 1, black),
            # Header/Produkte divider
            ('LINEBELOW', (0, 0), (-1, 0), 1, black),
            # Produkte/Kosten divider
            ('LINEBELOW', (0, h_produkte),
             (-1, h_produkte), 0.5, black),
            # Kosten/MwSt divider
            ('LINEBELOW', (0, h_produkte+h_kosten),
             (-1, h_produkte+h_kosten), 0.5, black),
            # MwSt/Footer divider
            ('LINEBELOW', (0, h_produkte+h_kosten+h_mwst),
             (-1, h_produkte+h_kosten+h_mwst), 1, black),
            # Footer
            ('LINEBELOW', (0, -1), (-1, -1), 1, black),

            # Span for total line
            ('SPAN', (0, -1-h_paycond), (2, -1-h_paycond)),

            # Horizontal alignment (same for all rows)
            ('ALIGN', (-1, 0), (-1, -1), "RIGHT"),
            ('ALIGN', (-2, 0), (-2, -1), "RIGHT"),
            ('ALIGN', (-4, 0), (-4, -1), "RIGHT"),
            # Vertical alignment (same for whole table)
            ('VALIGN', (0, 0), (-1, -1), "TOP"),
            # Bold total line
            ('FONTNAME', (0, -1-h_paycond), (-1, -1-h_paycond), "Helvetica-Bold"),
        ]

        return cls(data, repeatRows=1, style=TableStyle(style), colWidths=cls.COLWIDTHS)


class _PDFOrderProductTable(Table):
    COLWIDTHS = [36*mm, 110*mm, 20*mm, 20*mm]

    @classmethod
    def from_bestellung(cls, bestellung):
        sprache = bestellung.kunde.sprache if bestellung.kunde and bestellung.kunde.sprache else "de"

        data = [(_("Art-Nr."), _("Bezeichnung"), _("Anzahl"), _("Einheit"))]

        style_default = ParagraphStyle("Normal", fontname="Helvetica")
        style_bold = ParagraphStyle("Bold", fontname="Helvetica-Bold")

        produktanzahl = 0

        # Produkte
        for bp in bestellung.produkte.through.objects.filter(bestellung=bestellung):
            data.append((
                bp.produkt.artikelnummer,
                Paragraph(langselect(bp.produkt.name, sprache), style_default),
                str(bp.menge),
                langselect(autotranslate_mengenbezeichnung(bp.produkt.mengenbezeichnung), sprache),
            ))
            if bp.bemerkung:
                data.append((
                    "",
                    Paragraph("- "+bp.bemerkung, style_bold),
                    "",
                    ""
                ))

            produktanzahl += bp.menge

        data.append((  # Total
            _("ANZAHL PRODUKTE"),
            "",
            str(produktanzahl),
            ""
        ))

        style = TableStyle([
            ('LINEABOVE', (0, 0), (-1, 0), 1, black),
            ('LINEBELOW', (0, 0), (-1, 0), 1, black),
            ('LINEABOVE', (0, -1), (-1, -1), 1, black),
            ('LINEBELOW', (0, -1), (-1, -1), 1, black),
            ('ALIGN', (1, -1), (1, -1), "CENTER"),
            ('FONTNAME', (0, -1), (-1, -1), "Helvetica-Bold"),
            ('VALIGN', (0, 0), (-1, -1), "TOP"),
        ])

        return cls(data, repeatRows=1, style=style, colWidths=cls.COLWIDTHS)


class _PDFOrderQrInvoice(Flowable):
    @classmethod
    def from_bestellung(cls, bestellung, digital=True):
        elem = cls()
        elem.width = 210
        elem.height = 110
        elem._fixedWidth = 210
        elem._fixedHeight = 110
        elem.digital = digital
        elem.bestellung = bestellung
        return elem

    def __repr__(self):
        return "QR-Invoice"

    def __str__(self):
        return "QR-Invoice"

    def debug(self):
        c = self.canv
        c.setStrokeColor("green")
        c.rect(5*mm, 5*mm, 52*mm, 95*mm)  # Empfangsschein
        c.rect(67*mm, 5*mm, 138*mm, 95*mm)  # Zahlteil
        c.rect(67*mm, 42*mm, 46*mm, 46*mm)  # QR-Code
        c.line(5*mm, 23*mm, 57*mm, 23*mm)
        c.line(5*mm, 37*mm, 57*mm, 37*mm)
        c.line(5*mm, 93*mm, 57*mm, 93*mm)
        c.line(67*mm, 93*mm, 118*mm, 93*mm)
        c.line(67*mm, 37*mm, 118*mm, 37*mm)
        c.line(67*mm, 15*mm, 205*mm, 15*mm)
        c.line(118*mm, 100*mm, 118*mm, 15*mm)
        c.setStrokeColor("black")

    def get_swiss_qr_payload(self):
        bestellung = self.bestellung
        ze = bestellung.zahlungsempfaenger
        qrpayload = []

        def ln(text=""):
            qrpayload.append(text)

        # QRCH
        # - Header
        # - - QRType
        ln("SPC")
        # - - Version
        ln("0200")
        # - - Coding
        ln("1")

        # - CdtrInf (Empfänger)
        # - - IBAN
        if ze.mode == "QRR":
            ln(ze.qriban.replace(" ", ""))
        else:
            ln(ze.iban.replace(" ", ""))
        # - - Cdtr
        # - - - AdrTp
        ln("K")
        # - - - Name
        ln(ze.firmenname)
        # - - - StrtNmOrAdrLine1
        ln(ze.adresszeile1)
        # - - - BldgNbOrAdrLine2
        ln(ze.adresszeile2)
        # - - - PstCd
        ln()
        # - - - TwnNm
        ln()
        # - - - Ctry (2-stelliger Landescode gemäss ISO 3166-1)
        ln(ze.land)

        # - UltmtCdtr (Entgültiger Zahlungsempfänger)
        # - - AdrTp
        ln()
        # - - Name
        ln()
        # - - StrtNmOrAdrLine1
        ln()
        # - - BldgNbOrAdrLine2
        ln()
        # - - PstCd
        ln()
        # - - TwnNm
        ln()
        # - - Ctry (2-stelliger Landescode gemäss ISO 3166-1)
        ln()

        # - CcyAmt
        # - - Amt
        ln(formatprice(bestellung.fix_summe))
        # - - Ccy
        ln("CHF")

        # - UltmtDbtr (Entgültiger Zahlungspflichtiger)
        # - - AdrTp
        ln("K")
        # - - Name
        ln((bestellung.rechnungsadresse_vorname+" "+bestellung.rechnungsadresse_nachname)
           if not bestellung.rechnungsadresse_firma else bestellung.rechnungsadresse_firma)
        # - - StrtNmOrAdrLine1
        ln(bestellung.rechnungsadresse_adresszeile1)
        # - - BldgNbOrAdrLine2
        ln(bestellung.rechnungsadresse_plz+" "+bestellung.rechnungsadresse_ort)
        # - - PstCd
        ln()
        # - - TwnNm
        ln()
        # - - Ctry (2-stelliger Landescode gemäss ISO 3166-1)
        ln(bestellung.rechnungsadresse_land)

        # - RmtIn
        # - - TP
        ln(ze.mode)
        # - - Ref
        if ze.mode == "QRR":
            ln(bestellung.referenznummer().replace(" ", ""))
        else:
            ln()
        # - - AddInf
        # - - - Ustrd
        ln(bestellung.unstrukturierte_mitteilung())
        # - - - Trailer
        ln("EPD")
        # - - - StrdBkgInf
        ln(bestellung.rechnungsinformationen())

        ## - AltPmtInf
        ## - - AltPmt
        # ln()
        ## - - AltPmt
        # ln()

        return "\n".join(qrpayload)

    def draw_qr_invoice(self):
        bestellung = self.bestellung
        bestelldatum = str(bestellung.datum.strftime("%d.%m.%Y"))
        rechnungsinformationen = bestellung.rechnungsinformationen().split("/31/")
        referenznummer = bestellung.referenznummer()
        gesamtsumme = format(bestellung.fix_summe,
                             "08,.2f").replace(",", " ").lstrip(" 0")
        ze = bestellung.zahlungsempfaenger

        c = self.canv
        c.saveState()

        # QR-Code

        qrpayload = self.get_swiss_qr_payload()
        qr_code = qr.QrCodeWidget(qrpayload)
        qrbounds = qr_code.getBounds()
        qrwidth = qrbounds[2] - qrbounds[0]
        qrheight = qrbounds[3] - qrbounds[1]
        d = Drawing(
            52.2*mm, 52.2*mm, transform=[52.2*mm/qrwidth, 0, 0, 52.2*mm/qrheight, 0, 0])  # 46, 46
        d.add(qr_code)
        renderPDF.draw(d, c, 63.9*mm, 38.9*mm)  # 67, 42

        # Schweizerkreuz

        c.setFillColor("black")
        c.setStrokeColor("white")
        c.rect(86.5*mm, 61.5*mm, 7*mm, 7*mm, fill=1, stroke=1)
        c.setFillColor("white")
        c.rect(89.25*mm, 63*mm, 1.5*mm, 4*mm, fill=1, stroke=0)
        c.rect(88*mm, 64.25*mm, 4*mm, 1.5*mm, fill=1, stroke=0)

        c.setFillColor("black")
        c.setStrokeColor("black")

        # Begrenzungen Empfangsschein und Zahlteil und Abzutrennen-Hinweis

        if self.digital:
            c.line(0*mm, 105*mm, 210*mm, 105*mm)
            c.line(62*mm, 0*mm, 62*mm, 105*mm)
            c.setFont("Helvetica-Bold", 8)
            c.drawCentredString(
                105*mm, 107*mm, _("Vor der Einzahlung abzutrennen"))

        # Titel

        def titel(t, text, klein=False):
            t.setFont("Helvetica-Bold", 6 if klein else 8)
            t.textLine(text)
            t.moveCursor(0, 2)
            t.setFont("Helvetica", 8 if klein else 10)

        # Empfangsschein Angaben
        t = c.beginText(5*mm, 90*mm)
        titel(t, _("Konto / Zahlbar an"), True)
        t.textLine(ze.qriban if ze.mode == "QRR" else ze.iban)
        t.textLine(ze.firmenname)
        t.textLine(ze.adresszeile1)
        t.textLine(ze.adresszeile2)
        t.moveCursor(0, 9)
        if ze.mode == "QRR":
            titel(t, _("Referenz"), True)
            t.textLine(referenznummer)
            t.moveCursor(0, 9)
        titel(t, _("Zahlbar durch"), True)
        t.textLine((bestellung.rechnungsadresse_vorname+" "+bestellung.rechnungsadresse_nachname)
                   if not bestellung.rechnungsadresse_firma else bestellung.rechnungsadresse_firma)
        t.textLine(bestellung.rechnungsadresse_adresszeile1)
        t.textLine(bestellung.rechnungsadresse_plz +
                   " "+bestellung.rechnungsadresse_ort)
        c.drawText(t)

        # Zahlteil Angaben
        t = c.beginText(118*mm, 97*mm)
        titel(t, _("Konto / Zahlbar an"))
        t.textLine(ze.qriban if ze.mode == "QRR" else ze.iban)
        t.textLine(ze.firmenname)
        t.textLine(ze.adresszeile1)
        t.textLine(ze.adresszeile2)
        t.moveCursor(0, 9)
        if ze.mode == "QRR":
            titel(t, _("Referenz"))
            t.textLine(referenznummer)
            t.moveCursor(0, 9)
        titel(t, _("Zusätzliche Informationen"))
        t.textLine(bestellung.unstrukturierte_mitteilung())
        t.textLine(rechnungsinformationen[0])
        t.textLine("/31/"+rechnungsinformationen[1])
        t.moveCursor(0, 9)
        titel(t, _("Zahlbar durch"))
        t.textLine((bestellung.rechnungsadresse_vorname+" "+bestellung.rechnungsadresse_nachname)
                   if not bestellung.rechnungsadresse_firma else bestellung.rechnungsadresse_firma)
        t.textLine(bestellung.rechnungsadresse_adresszeile1)
        t.textLine(bestellung.rechnungsadresse_plz +
                   " "+bestellung.rechnungsadresse_ort)
        c.drawText(t)

        # Texte
        c.setFont("Helvetica-Bold", 11)
        c.drawString(5*mm, 97*mm, _("Empfangsschein"))
        c.drawString(67*mm, 97*mm, _("Zahlteil"))

        c.setFont("Helvetica-Bold", 6)
        c.drawString(5*mm, 33*mm, _("Währung"))
        c.drawString(20*mm, 33*mm, _("Betrag"))
        c.drawString(38*mm, 20*mm, _("Annahmestelle"))

        c.setFont("Helvetica", 8)
        c.drawString(5*mm, 30*mm, "CHF")
        c.drawString(20*mm, 30*mm, gesamtsumme)

        c.setFont("Helvetica-Bold", 8)
        c.drawString(67*mm, 33*mm, _("Währung"))
        c.drawString(87*mm, 33*mm, _("Betrag"))

        c.setFont("Helvetica", 10)
        c.drawString(67*mm, 29*mm, "CHF")
        c.drawString(87*mm, 29*mm, gesamtsumme)

        # c.setFont("Helvetica-Bold", 7)
        # c.drawString(67*mm, 11*mm, "Name AV1:")
        # c.drawString(67*mm, 8*mm, "Name AV2:")
        #
        # c.setFont("Helvetica", 7)
        # c.drawString(82*mm, 11*mm, "Linie 1")
        # c.drawString(82*mm, 8*mm, "Linie 2")

        # if settings.DEBUG:
        # self.debug()

        c.restoreState()

    def draw(self):
        self.canv.translate(-12*mm, -12*mm)
        self.draw_qr_invoice()


class _PDFOrderHeader(Flowable):
    @classmethod
    def from_bestellung(cls, bestellung, lieferschein=False):
        elem = cls()
        elem.width = 210
        elem.height = 75
        elem._fixedWidth = 210
        elem._fixedHeight = 75
        elem.lieferschein = lieferschein
        elem.bestellung = bestellung
        return elem

    def __repr__(self):
        return "QR-Invoice"

    def __str__(self):
        return "QR-Invoice"

    def draw_header(self):
        bestellung = self.bestellung
        bestelldatum = str(bestellung.datum.strftime("%d.%m.%Y"))
        ze = bestellung.zahlungsempfaenger

        c = self.canv
        c.saveState()

        # Logo
        if ze.logourl:
            c.drawImage(ImageReader(ze.logourl), 120*mm, 67*mm,
                        width=20*mm, height=-20*mm, mask="auto", anchor="nw")

        # Firmenname
        c.setFont("Helvetica-Bold", 14)
        c.drawString(12*mm, 64*mm, ze.firmenname)

        # Firmenadresse
        t = c.beginText(12*mm, 57*mm)
        t.setFont("Helvetica", 10)
        t.textLine(ze.adresszeile1)
        t.textLine((ze.land+"-" if not ze.land ==
                    "CH" else "")+ze.adresszeile2)
        c.drawText(t)

        # Firmendaten: Texte
        t = c.beginText(12*mm, 46*mm)
        t.setFont("Helvetica", 8)
        t.textLine(_("Tel."))
        t.textLine(_("E-Mail"))
        if ze.webseite:
            t.textLine(_("Web"))
        if ze.firmenuid:
            t.textLine(_("MwSt"))
        c.drawText(t)

        # Firmendaten: Inhalt
        t = c.beginText(24*mm, 46*mm)
        t.setFont("Helvetica", 8)
        t.textLine(bestellung.ansprechpartner.telefon)
        t.textLine(bestellung.ansprechpartner.email)
        if ze.webseite:
            t.textLine(ze.webseite)
        if ze.firmenuid:
            t.textLine(ze.firmenuid)
        c.drawText(t)

        # Rechnungsdaten: Texte
        t = c.beginText(12*mm, 27*mm)
        t.setFont("Helvetica", 12)
        t.textLine(_("Ihr/e Ansprechpartner/in"))
        t.textLine(_("Ihre Kundennummer"))
        t.textLine(_("Ihre Bestellung vom"))
        if not self.lieferschein:
            t.textLine(_("Rechnungsdatum"))
        c.drawText(t)

        # Rechnungsdaten: Inhalt
        t = c.beginText(64*mm, 27*mm)
        t.setFont("Helvetica", 12)
        t.textLine(bestellung.ansprechpartner.name)
        t.textLine(bestellung.kunde.pkfill(6)
                   if bestellung.kunde else "n.a.")
        t.textLine(bestelldatum)
        if not self.lieferschein:
            t.textLine(
                (bestellung.rechnungsdatum or bestellung.datum).strftime("%d.%m.%Y"))
        c.drawText(t)

        # Kundenadresse
        t = c.beginText(120*mm, 27*mm)
        t.setFont("Helvetica", 12)
        if self.lieferschein:
            if bestellung.lieferadresse_firma:
                t.textLine(bestellung.lieferadresse_firma)
            if bestellung.lieferadresse_vorname or bestellung.lieferadresse_nachname:
                t.textLine(
                    f'{bestellung.lieferadresse_vorname} {bestellung.lieferadresse_nachname}'.strip())
            t.textLine(bestellung.lieferadresse_adresszeile1)
            if bestellung.lieferadresse_adresszeile2:
                t.textLine(bestellung.lieferadresse_adresszeile2)
            t.textLine(
                f'{bestellung.lieferadresse_plz} {bestellung.lieferadresse_ort}'.strip())
        else:
            if bestellung.rechnungsadresse_firma:
                t.textLine(bestellung.rechnungsadresse_firma)
            if bestellung.rechnungsadresse_vorname or bestellung.rechnungsadresse_nachname:
                t.textLine(
                    f'{bestellung.rechnungsadresse_vorname} {bestellung.rechnungsadresse_nachname}'.strip())
            t.textLine(bestellung.rechnungsadresse_adresszeile1)
            if bestellung.rechnungsadresse_adresszeile2:
                t.textLine(bestellung.rechnungsadresse_adresszeile2)
            t.textLine(
                f'{bestellung.rechnungsadresse_plz} {bestellung.rechnungsadresse_ort}'.strip())
        c.drawText(t)

        # Rechnung
        c.setFont("Helvetica-Bold", 10)
        if self.lieferschein:
            c.drawString(12*mm, 0*mm, _("LIEFERSCHEIN"))
        else:
            c.drawString(
                12*mm, 0*mm, self.bestellung.rechnungstitel or _("RECHNUNG"))

        c.setFont("Helvetica", 10)
        if not (bestellung.rechnungstitel and len(bestellung.rechnungstitel) > 20):
            c.drawString(64*mm, 0*mm, f'{bestellung.datum.year}-{bestellung.pkfill(6)}' +
                         (f' (Online #{bestellung.woocommerceid})' if bestellung.woocommerceid else ''))

        c.restoreState()

    def draw(self):
        self.canv.translate(-12*mm, -40*mm)
        self.draw_header()


class PDFOrder(PDFGenerator):
    def get_elements(self, bestellung, lieferschein=False, digital: bool = True):
        bestellung.fix_summe = bestellung.summe_gesamt()

        # Header
        elements = [
            _PDFOrderHeader.from_bestellung(
                bestellung, lieferschein=lieferschein),
            Spacer(1, 48*mm),
        ]

        # Invoice text
        if bestellung.rechnungstext:
            elements += [
                Paragraph(bestellung.rechnungstext.replace("\n", "\n<br />")),
                Spacer(1, 10*mm),
            ]

        # Main body
        if lieferschein:
            elements += [
                _PDFOrderProductTable.from_bestellung(bestellung)
            ]
        else:
            elements += [
                _PDFOrderPriceTable.from_bestellung(bestellung),
                Spacer(1, 65*mm),
                TopPadder(_PDFOrderQrInvoice.from_bestellung(
                    bestellung, digital))
            ]

        return elements

    def get_language(self, bestellung, *args, **kwargs):
        return bestellung.kunde.sprache if bestellung.kunde and bestellung.kunde.sprache else "de"
