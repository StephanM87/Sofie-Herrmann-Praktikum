from pylatex import Document, Tabular, Section, NoEscape, Command, MultiRow
from Old.BioCatHubDatenmodell import DataModel

first_name = "some firstname"
last_name = "some lastname"
e_mail = "some@adress.com"
institution = "some institution"
vessel_type = "some vessel"
volume = int(42)
vol_unit = "mol/l"
add_attributes = [{"Sektor": "Kruzifix"}, {"Bereich": "Eisheiligen"}]
temp = int(42)
temp_unit = "°C"
ph_value = int(7)
buffer = "some buffer"


class PdfLibrary (Document):

    def __init__(self, data_model):
        self.biocathub_model = data_model

    def create_pdf(self):
        geometry_options = {
            "margin": "2cm",
            "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)

        doc.preamble.append(Command("title", self.biocathub_model["title"]))
        doc.append(NoEscape(r"\maketitle"))

        with doc.create(Section("User:")):
            with doc.create(Tabular("|c|c|")) as table:
                table.add_hline()
                table.add_row(["First Name", first_name])
                table.add_hline()
                table.add_row(["Last Name", last_name])
                table.add_hline()
                table.add_row(["E-Mail", e_mail])
                table.add_hline()
                table.add_row(["Institution", institution])
                table.add_hline()
        with doc.create(Section("Vessel:")):
            with doc.create(Tabular("|c|c|")) as table2:
                for i in DataModel["vessel"]:
                    key = list(i.keys())
                    table2.add_row([key, i[key]])
                    table2.add_hline()
        with doc.create(Section("Condition:")):
            with doc.create(Tabular("|c|c|")) as table3:
                table3.add_hline()
                table3.add_row(["Temperature", temp])
                table3.add_hline()
                table3.add_row(["Unit", temp_unit])
                table3.add_hline()
                table3.add_row(["pH", ph_value])
                table3.add_hline()
                table3.add_row(["Buffer", buffer])
                table3.add_hline()
                for i in add_attributes:
                    key = list(i.keys())[0]
                    table3.add_row([key, i[key]])
                    table3.add_hline()

        doc.generate_pdf("Gesamt_Test",
                         compiler="pdflatex", clean_tex=False)


doc = PdfLibrary(DataModel)
doc.create_pdf()
