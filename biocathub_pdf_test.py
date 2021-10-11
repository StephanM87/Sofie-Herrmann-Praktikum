import pylatex.config as cf
from pylatex import Document, Tabular, Section, Subsection, NoEscape, Command
from BioCatHubDatenmodell import DataModel

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
                def kack_funktion(dict):
                    print(dict["key"], dict["value"])

                for i in self.biocathub_model["condition"]["others"]:
                    kack_funktion(i)

        with doc.create(Subsection("Buffer")):
                    with doc.create(Tabular("|c|c|")) as table3_1:
                        table3_1.add_hline()
                        for i in buffer_dict_entries:
                            table3_1.add_row([i["label"], self.biocathub_model["condition"]["buffer"][i["key"]]])
                            table3_1.add_hline()
        
        '''with doc.create(Section("Enzymes")):
            with doc.create(Tabular("|c|c|")) as table4:
                table4.add_hline()
                def ausgabe(dict):
                    print(dict["concentration"], dict["ecNUmber"])
                def extract_dict(dict):
                    enzymes = dict[self.biocathub_model["enzymes"]]
                    for i in enzymes:
                        ausgabe(i)
                for i in self.biocathub_model["enzymes"]:
                    extract_dict(i)'''

                
        doc.generate_pdf("biocathub_pdf_test",
                         compiler="pdflatex", clean_tex=False)


doc = PdfLibrary(DataModel)
doc.create_pdf()
