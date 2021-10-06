from pylatex import Document, LongTable, MultiColumn, Section
from Old.BioCatHubDatenmodell import DataModel


class SomeClass(Document):

    def __init__(self, data_model):
        self.biocathub_model = data_model

    '''
        This class makes ich hab keine Ahnung and takes the following parameters:

        a = int
        b = String

        The retun value is:
        x = List
    '''

    def printModel(self):
        print(self.biocathub_model["title"])

    def create_table(self):

        geometry_options = {
            "margin": "2.5cm",
            "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)

        with doc.create(Section("Eine wunderschöne Tabelle")):
            with doc.create(LongTable("c c")) as table:
                table.add_hline()
                table.add_row(["Ungerade Zahlen", "Gerade Zahlen"])
                table.add_hline()
                table.end_table_header()
                table.add_hline()
                table.add_row((MultiColumn(2),))
                table.add_hline()
                table.end_table_footer()
                table.add_hline()
                table.add_row((MultiColumn(2),))
                table.add_hline()
                table.end_table_last_footer()
                row = [["1", "2"], ["3", "4"],
                       ["5", "6"], ["7", "8"]]
                for i in row:
                    table.add_row(i)
            doc.generate_pdf("TEST", compiler="pdflatex", clean_tex=False)

doc = SomeClass(DataModel)
doc.printModel()

