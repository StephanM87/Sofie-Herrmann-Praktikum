from pylatex import Document, Tabular, Section, NoEscape, Command, MultiRow
from Old.BioCatHubDatenmodell import DataModel

class PdfLibrary (Document):

    def __init__(self, data_model):
        self.biocathub_model = data_model

    def create_pdf(self):
        geometry_options = {
            "margin": "2.54cm",
            "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)

        doc.preamble.append(Command("title", self.biocathub_model["title"]))
        doc.append(NoEscape(r"\maketitle"))

        with doc.create(Section("User:")):
            with doc.create(Tabular("|c|c|")) as table:
                table.add_hline()
                table.add_row(["E-Mail", self.biocathub_model["user"]["email"]])
                table.add_hline()
                table.add_row(["First Name", self.biocathub_model["user"]["firstName"]])
                table.add_hline()
                table.add_row(["Last Name", self.biocathub_model["user"]["lastName"]])
                table.add_hline()
                table.add_row(["Institution", self.biocathub_model["user"]["institution"]])
                table.add_hline()
        with doc.create(Section("Vessel:")):
            with doc.create(Tabular("|c|c|")) as table2:
                table2.add_hline()
                table2.add_row(["Type", self.biocathub_model["vessel"]["type"]])
                table2.add_hline()
                table2.add_row(["Unit", self.biocathub_model["vessel"]["unit"]])
                table2.add_hline()
                table2.add_row(["Volume", self.biocathub_model["vessel"]["volume"]])
                table2.add_hline()
                for i in self.biocathub_model["vessel"]["others"]:
                    key = list(i.keys())[0]
                    table2.add_row([key, i[key]])
                    table2.add_hline()
        with doc.create(Section("Condition:")):
            with doc.create(Tabular("|c|c|")) as table3:
                table3.add_hline()
                table3.add_row(["Temperature", self.biocathub_model["condition"]["temp"]])
                table3.add_hline()
                table3.add_row(["Unit", self.biocathub_model["condition"]["unit"]])
                table3.add_hline()
                table3.add_row(["pH", self.biocathub_model["condition"]["ph"]])
                table3.add_hline()
                table3.add_row(["Buffer Concentration", self.biocathub_model["condition"]["buffer"]["concentration"]])
                table3.add_hline()
                table3.add_row(["Buffer Type", self.biocathub_model["condition"]["buffer"]["type"]])
                table3.add_hline()
                table3.add_row(["Buffer Unit", self.biocathub_model["condition"]["buffer"]["unit"]])
                table3.add_hline()
                for i in self.biocathub_model["condition"]["others"]:
                    key = list(i.keys())[0]
                    table3.add_row([key, i[key]])
                    table3.add_hline()

        doc.generate_pdf("biocathub_pdf_test",
                         compiler="pdflatex", clean_tex=False)


doc = PdfLibrary(DataModel)
doc.create_pdf()
