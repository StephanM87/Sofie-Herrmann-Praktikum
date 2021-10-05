from pylatex import Document, Subsection, LongTable, MultiColumn, NoEscape, Section, Command, Figure, Tabular, MultiRow
import pylatex.config as cf

bild = "glees.jpg"
bild2 = "Klettern in Glees.jpg"
text =  '''Im Bouldergebiet Glees auf dem Gebiet der Gemeinde Wassenach in der Osteifel wird seit den 80er Jahren geklettert. Das Gebiet zieht sich in einem Waldstück entlang eines Hangs über 2km hin.
Das Basanit genannte Gestein entstammt einem Ausbruch des Vulkans Veitskopf. Es ist dank Einschlüssen kleiner Quarzkristalle sehr rau und dadurch enorm hautintensiv. Die Kletterei ist geprägt von Leisten an Säulen, die – mal näher, mal weiter – nebeneinanderstehend die Abbruchkante des Lavastroms bilden. Es gibt mittlerweile über 300 erschlossene Linien.'''

class Glees(Document):

    def create_table(self):
        geometry_options = {
             "margin": "2cm",
             "includeheadfoot": True
        }
        doc = Document(page_numbers=True, geometry_options=geometry_options)
        
        doc.preamble.append(Command("title", "Glees - Das beste Bouldergebiet der Welt"))
        doc.append(NoEscape(r"\maketitle"))

        with doc.create(Section("Ein Bild vom Veitskopf")):
             with doc.create(Figure(position="h!")) as glees_picture:
                 glees_picture.add_image(bild, width="480px")
                 glees_picture.add_caption("Super coole Bildbeschreibung")

        with doc.create(Section("Ein bisschen Text")):
             with doc.create(Subsection("Zu 100% von der Website runterkopiert")):
                  cf.active = cf.Version1()
                  doc.append(text)
             with doc.create(Figure(position="h!")) as glees_picture2:
                 glees_picture2.add_image(bild2, width="240px")
                 glees_picture2.add_caption("Klettern in Glees macht Spaß")

        with doc.create(Section("Grade")):
             doc.append("Alle Boulder sind mit einem Pfeil in entsprechender Farbe markiert.")
             with doc.create(LongTable("c c")) as data_table:
                data_table.add_hline()
                data_table.add_row(["Pfeilfarbe", "fb-Grad"])
                data_table.add_hline()
                data_table.end_table_header()
                data_table.add_hline()
                data_table.add_row((MultiColumn(2),))
                data_table.add_hline()
                data_table.end_table_footer()
                data_table.add_hline()
                data_table.add_row((MultiColumn(2),))
                data_table.add_hline()
                data_table.end_table_last_footer()
                row = [["gelb", "3a - 4b"],["blau", "4b - 5b"],
                      ["rot", "5c - 6b"], ["weiß", "6b+ - 8a"]]
                for i in row:
                    data_table.add_row(i)

        with doc.create(Section("Eine Tabelle")):
             with doc.create(Subsection("Sektoren und Bereiche")):
                  with doc.create(Tabular("|c|c|")) as table2:
                      table2.add_hline()
                      table2.add_row(["Sektoren","Bereiche"])
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Bleausard"),"Osterinsel"))
                      table2.add_hline(2)
                      table2.add_row(("","Bleausardblock"))
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Mauerlay"),"Balrock"))
                      table2.add_hline(2)
                      table2.add_row("", "Rübennase")
                      table2.add_hline(2)
                      table2.add_row("", "Megalopolis")
                      table2.add_hline(2)
                      table2.add_row("", "Rush More")
                      table2.add_hline(2)
                      table2.add_row("", "Supra Arbor")
                      table2.add_hline(2)
                      table2.add_row("", "Kamel")
                      table2.add_hline(2)
                      table2.add_row("", "Bescherung")
                      table2.add_hline(2)
                      table2.add_row("", "Mauerlay")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Kruzifix"),"Elefant"))
                      table2.add_hline(2)
                      table2.add_row("", "Kreuzfels")
                      table2.add_hline(2)
                      table2.add_row("", "Eisheiligen")
                      table2.add_hline(2)
                      table2.add_row("", "Tiefflieger")
                      table2.add_hline(2)
                      table2.add_row("", "Löwenherz")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Lichtung"),"Bromarma"))
                      table2.add_hline(2)
                      table2.add_row("", "Krokodil")
                      table2.add_hline(2)
                      table2.add_row("", "Lawine")
                      table2.add_hline(2)
                      table2.add_row("", "Lichtung")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Romani Ite Domum"),"The Egg"))
                      table2.add_hline(2)
                      table2.add_row("", "Forum")
                      table2.add_hline(2)
                      table2.add_row("", "Römerturm")
                      table2.add_hline(2)
                      table2.add_row("", "Es")
                      table2.add_hline(2)
                      table2.add_row("", "Windei")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Labyrinth"),"Die Macht"))
                      table2.add_hline(2)
                      table2.add_row("", "Steinzeit")
                      table2.add_hline(2)
                      table2.add_row("", "Here Be Dragons")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Terra Incognita"),"Voyger"))
                      table2.add_hline(2)
                      table2.add_row("", "Humboldt")
                      table2.add_hline(2)
                      table2.add_row("", "Newton")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="Mordor"),"Kamikaze"))
                      table2.add_hline(2)
                      table2.add_row("", "Camelot")
                      table2.add_hline(2)
                      table2.add_row("", "Almost Satan")
                      table2.add_hline(2)
                      table2.add_row("", "Cosmos")
                      table2.add_hline(2)
                      table2.add_row("", "Orodruin")
                      table2.add_hline(2)
                      table2.add_row("", "Barad Dur")
                      table2.add_hline(2)
                      table2.add_row("", "Gondor")
                      table2.add_hline()
                      table2.add_row((MultiRow(2, data="West- und Südblöcke"),"Orthank"))
                      table2.add_hline(2)
                      table2.add_row("", "Macchu Picchu")
                      table2.add_hline(2)
                      table2.add_row("", "Südblöcke")
                      table2.add_hline()
       
        doc.generate_pdf("Glees_Versuch3", compiler="pdflatex", clean_tex=False)
        
doc = Glees()
doc.create_table()
