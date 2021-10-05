from pylatex import Document, Tabular, Section, NoEscape, Command, MultiRow

title_name = "Super cooler Titel"
first_name = "some firstname"
last_name = "some lastname"
e_mail = "some@adress.com"
institution = "some institution"
vessel_type = "some vessel"
volume = int(42)
vol_unit = "mol/l"
additional_attributes = ["a","s", "d", "f"]
add_attributes = [{"Sektor":"Kruzifix"}, {"Bereich":"Eisheiligen"}]
temp = int(42)
temp_unit = "°C"
ph_value = int(7)
buffer = "some buffer"
additional_attributes2 = ["a", "b", "c"]


class PdfLibrary (Document):
    def create_pdf (self):
        geometry_options = {
             "margin": "2cm",
             "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)
        
        doc.preamble.append(Command("title", title_name))
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
                      table2.add_hline()
                      table2.add_row(["Type", vessel_type])
                      table2.add_hline()
                      table2.add_row(["Volume", volume])
                      table2.add_hline()
                      table2.add_row(["Unit", vol_unit])
                      table2.add_hline()
                      for i in add_attributes:
                          key = list(i.keys())[0]
                          print(key)
                          table2.add_row([key, i[key]])
                          table2.add_hline()

                      table2.add_row((MultiRow(2, data = "Others"), additional_attributes[0]))
                      for i in additional_attributes:
                          table2.add_hline(2)
                          table2.add_row("", i)
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
                      table3.add_row((MultiRow(2, data = "Others"), additional_attributes2[0]))
                      for i in additional_attributes2:
                          table3.add_hline(2)
                          table3.add_row("", additional_attributes2[0])
                      table3.add_hline()
        
        doc.generate_pdf("Gesamt Versuch5", compiler="pdflatex", clean_tex=False)

doc = PdfLibrary()
doc.create_pdf()