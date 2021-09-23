from pylatex import Document, LongTable, MultiColumn, LongTabu, Tabu

class GleesDocument(Document):
    def table(self):
        geometry_options = {
             "margin": "2.54cm",
             "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)

        fmt = "X[r] X[r] X[r]"
        with doc.create(LongTable(fmt)) as glees_table:
                glees_table.add_hline()
                glees_table.add_row(["Nummer", "Grund", "asdf"])
                glees_table.add_hline()
                glees_table.end_table_header()
                glees_table.add_hline()
                glees_table.add_row((MultiColumn(3, align='r')))
                glees_table.add_hline()
                glees_table.end_table_footer()
                glees_table.add_hline()
                glees_table.add_row((MultiColumn(3, align='r')))
                glees_table.add_hline()
                glees_table.end_table_last_footer()
                row = ["text1", "text2", "text3"]
                for i in range(10):
                    glees_table.add_row(row)

if __name__ == "__main__":
    doc = GleesDocument()
    doc.table()
    doc.generate_pdf("Glees_ist_geil", clean_tex=False)