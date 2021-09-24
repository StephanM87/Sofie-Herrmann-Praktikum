from pylatex import Document, LongTable, MultiColumn, LongTabu, Tabu

class GleesDocument(Document):
    def table(self):
        geometry_options = {
             "margin": "2.54cm",
             "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)

        fmt = "X[r] X[r] X[r]"
        with doc.create(LongTable(fmt)) as data_table:
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
                row = ["Sophie", "Glees", "Bouldern"]
                for i in range(15):
                    data_table.add_row(row)
        doc.generate_pdf("gleesiglees",compiler="pdflatex", clean_tex=False)

#if __name__ == "__main__":
doc = GleesDocument()
doc.table()
#doc.generate_pdf("gleesiglees",compiler="pdflatex", clean_tex=False)
print("guten Morgen")