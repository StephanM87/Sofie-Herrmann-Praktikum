from pylatex import Document, Section, Figure, LongTable, MultiColumn

image_name = "glees.jpg"

class GleesPDF(Document):
    def image(self):
        geometry_options = {
            "margin": "2.5"
            }
        doc = Document(geometry_options=geometry_options)

        with doc.create(Section("Glees",numbering=False)):
             with doc.create(Figure(position="h!")) as glees_picture:
                 glees_picture.add_image(image_name, width="480px")
                 glees_picture.add_caption("super coole bildbeschreibung")
        doc.generate_pdf("Teil1", compiler = "pdflatex", clean_tex=False)           

    def table(self):
        geometry_options = {
             "margin": "2.54cm",
             "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)
        
        with doc.create(LongTable("l l l")) as data_table:
                data_table.add_hline()
                data_table.add_row(["Nummer", "Grund", "asdf"])
                data_table.add_hline()
                data_table.end_table_header()
                data_table.add_hline()
                data_table.add_row((MultiColumn(3, align='r',
                                    data='Continued on Next Page'),))
                data_table.add_hline()
                data_table.end_table_footer()
                data_table.add_hline()
                data_table.add_row((MultiColumn(3, align='r',
                                    data='Not Continued on Next Page'),))
                data_table.add_hline()
                data_table.end_table_last_footer()
                row = [["1", "Terassen nach GTN", "Bouldern"],["2", "Handyempfang am Fels", "Bouldern2"],
                      ["3", "Beste Tankstelle der Welt", "Bouldern3"]]
                for i in row:
                        data_table.add_row(i)

        doc.generate_pdf("Teil2",compiler="pdflatex", clean_tex=False)

doc = GleesPDF()
doc.table()
doc.image()