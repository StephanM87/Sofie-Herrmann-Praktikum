from pylatex import Document, Section, Subsection, Figure
import os

image_name = os.path.join(os.path.dirname("C:\home\sofie\Desktop\glees test\glees.jpg"))

class GleesBild(Document):
    def image(self):
        geometry_options = {
            "tmargin": "1cm",
            "lmargin": "10cm"
            }
        doc = Document(geometry_options=geometry_options)

        with doc.create(Subsection("eine bildbeschreibung")):
             with doc.create(Figure(position="h!")) as glees_picture:
                 glees_picture.add_image(image_name, width="120px")
                 glees_picture.add_caption("super coole bildbeschreibung")

if __name__ == "__main__":
    doc = GleesBild()
    doc.image()
    doc.generate_pdf("bild", clean_tex=False)
