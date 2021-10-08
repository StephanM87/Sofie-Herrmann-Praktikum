import pylatex.config as cf
from pylatex import Document, Tabular, Section, NoEscape, Command, MultiRow
from Old.BioCatHubDatenmodell import DataModel

user_dict_entries = [
                    {"key":"email",
                    "label":"E-Mail"},
                    {"key":"firstName",
                    "label":"First Name"},
                    {"key":"lastName",
                    "label":"Last Name"},
                    {"key":"institution",
                    "label":"Institute"}
                ]
vessel_dict_entries = [
                      {"key":"type",
                      "label":"Vesseltype"},
                      {"key":"unit",
                      "label":"Unit"},
                      {"key":"volume",
                      "label":"Volume"},
                      {"key":"others",
                      "label":"Additional"}

                ]

condition_dict_entries = [
                      {"key":"ph",
                      "label":"pH"},
                      {"key":"temp",
                      "label":"Temperature"},
                      {"key":"unit",
                      "label":"Unit"},
                      {"key":"buffer",
                      "label":"Buffer"},
                      {"key": "others",
                      "label":"Additional"}

                ]

buffer_dict_entries = [
                      {"key":"concentration",
                      "label":"Concentration"},
                      {"key":"type",
                      "label":"Buffertype"},
                      {"key":"unit",
                      "label":"Unit"}

                ]

enzymes_dict_entries = [
                      {"key":"concentration",
                      "label":"Concentration"},
                      {"key":"ecNumber",
                      "label":"ecNumber"},
                      {"key":"formulation",
                      "label":"Formulation"},
                      {"key":"method",
                      "label":"Method"},
                      {"key":"name",
                      "label":"Name"},
                      {"key":"organism",
                      "label":"Organism"},
                      {"key":"sequence",
                      "label":"Sequence"},
                      {"key":"type",
                      "label":"Type"},
                      {"key":"unit",
                      "label":"Unit"},
                      {"key":"variant",
                      "label":"Variant"}


                ]

measurements_dict_entries = [
                      {"key":"notes",
                      "label":"Notes"},
                      {"key":"plotStyle",
                      "label":"Plot Style"},
                      {"key":"reagent",
                      "label":"Reagent"},
                      {"key":"replicates",
                      "label":"Replicates"}

                ]


class PdfLibrary (Document):

    def __init__(self, data_model):
        self.biocathub_model = data_model

    def create_pdf(self):
        geometry_options = {
            "margin": "2.54cm",
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)

        doc.preamble.append(Command("title", self.biocathub_model["title"]))
        doc.append(NoEscape(r"\maketitle"))

        with doc.create(Section("Description")):
            cf.active = cf.Version1()
            doc.append(self.biocathub_model["description"])

        with doc.create(Section("User:")):
            with doc.create(Tabular("|c|c|")) as table:
                table.add_hline()
                for i in user_dict_entries:
                    table.add_row([i["label"], self.biocathub_model["user"][i["key"]]])
                    table.add_hline()

        with doc.create(Section("Vessel:")):
            with doc.create(Tabular("|c|c|")) as table2:
                table2.add_hline()
                for i in vessel_dict_entries:
                    table2.add_row([i["label"], self.biocathub_model["vessel"][i["key"]]])
                    table2.add_hline()

        with doc.create(Section("Condition:")):
            with doc.create(Tabular("|c|c|")) as table3:
                table3.add_hline()
                for i in condition_dict_entries:
                    table3.add_row([i["label"], self.biocathub_model["condition"][i["key"]]])
                    table3.add_hline()
                for j in buffer_dict_entries:
                    table3.add_row([j["label"], self.biocathub_model["condition"]["buffer"][j["key"]]])
                    table3.add_hline()
        
        '''with doc.create(Section("Enzymes")):
            with doc.create(Tabular("|c|c|")) as table4:
                table4.add_hline()
                for i in enzymes_dict_entries:
                    table4.add_row([i["label"], self.biocathub_model["enzymes"][i["key"]]])
                    table4.add_hline()'''
        
        ''''with doc.create(Section("Experimental Data:")):
            with doc.create(Tabular("|c|c|")) as table5:
                table5.add_hline()
                for i in measurements_dict_entries:
                    table5.add_row([i["label"], self.biocathub_model["experimentalData"]["measurements"][i["key"]]])
                    table5.add_hline()'''

        doc.generate_pdf("biocathub_pdf_test2",
                         compiler="pdflatex", clean_tex=False)


doc = PdfLibrary(DataModel)
doc.create_pdf()