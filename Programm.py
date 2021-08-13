#!/usr/bin/env python
# coding: utf-8

# In[34]:


class Enzyme():
    def __init__(self, name, as_sequence, concentration, unit):
        self.name = name
        self.as_sequence = as_sequence
        self.concentration = concentration
        self.unit = unit

class Show_Enzyme(Enzyme):
    def __init__(self, name, as_sequence, concentration, unit):
        super().__init__(name, as_sequence, concentration, unit)
    def show(self):
        return self.name + ", " + self.as_sequence + ", " + self.concentration + ", " + self.unit
test = Show_Enzyme("Aconitate Hydratase", "IHETHE", 0.1, "mol/l")
try:
    print(test.show())
except TypeError:
    print("Falscher Datentyp")
    