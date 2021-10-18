import pylatex.config as cf
from pylatex import Document, Tabular, Section, Subsection, NoEscape, Command, MultiRow
from Old.BioCatHubDatenmodell import DataModel
from dict_entries import user_dict_entries, vessel_dict_entries, condition_dict_entries, buffer_dict_entries, enzymes_dict_entries, educts_dict_entries


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
                user = self.biocathub_model["user"]
                table.add_hline()
                for i in user_dict_entries:
                    table.add_row([i["label"], user[i["key"]]])
                    table.add_hline()

        with doc.create(Section("Vessel:")):
            with doc.create(Tabular("|c|c|")) as table2:
                vessel = self.biocathub_model["vessel"]
                table2.add_hline()
                for i in vessel_dict_entries:
                    table2.add_row([i["label"], vessel[i["key"]]])
                    table2.add_hline()
                def add_others(dict):
                    for i in dict:
                        table2.add_row(["Other", [dict[i]]])
                        table2.add_hline()

                for i in vessel["others"]:
                    add_others(i)

        with doc.create(Section("Condition:")):
            with doc.create(Tabular("|c|c|")) as table3:
                condition = self.biocathub_model["condition"]
                table3.add_hline()
                for i in condition_dict_entries:
                    table3.add_row([i["label"], condition[i["key"]]])
                    table3.add_hline()
                def kack_funktion(dict):
                    for i in dict:
                        table3.add_row((MultiRow(1, data = "Other"), dict[i]))
                        table3.add_row("", "")
                        table3.add_hline(2)

                for i in condition["others"]:
                    kack_funktion(i)
                    table3.add_hline()

        with doc.create(Subsection("Buffer")):
                    with doc.create(Tabular("|c|c|")) as table3_1:
                        buffer = self.biocathub_model["condition"]["buffer"]
                        table3_1.add_hline()
                        for i in buffer_dict_entries:
                            table3_1.add_row([i["label"], buffer[i["key"]]])
                            table3_1.add_hline()
        
        with doc.create(Section("Enzymes")):
            with doc.create(Tabular("|c|c|")) as table4:
                enzymes = self.biocathub_model["enzymes"]
                table4.add_hline()
                def kack_funktion2(dict):
                    for i in dict:
                        table4.add_row([i, dict[i]])
                        table4.add_hline()

                for i in enzymes:
                    kack_funktion2(i)
        
        with doc.create(Subsection("Educts")):
            with doc.create(Tabular("|c|c|")) as table4_1:
                enzyme_container = i
                educts = enzyme_container["reaction"]["educts"]
                table4_1.add_hline()
                def verfickte_drecks_funktion(dict):
                    for i in dict:
                        table4_1.add_row([i, dict[i]])
                        table4_1.add_hline()
 
                for i in educts:
                    verfickte_drecks_funktion(i)

        with doc.create(Subsection("Products")):
            with doc.create(Tabular("|c|c|")) as table4_2:
                products = enzyme_container["reaction"]["products"]
                table4_2.add_hline()
                def verfickte_drecks_funktion2(dict):
                    for i in dict:
                        table4_2.add_row([i, dict[i]])
                        table4_2.add_hline()
                        #print(dict[i])
 
                for i in products:
                    verfickte_drecks_funktion2(i)

        with doc.create(Subsection("Value")):
            cf.active = cf.Version1()
            def please_work(dict):
                    doc.append(dict["reaction"]["value"])
            
            for i in self.biocathub_model["enzymes"]:
                please_work(i)

        doc.generate_pdf("biocathub_pdf_test",
                         compiler="pdflatex", clean_tex=False)


doc = PdfLibrary(DataModel)
doc.create_pdf()