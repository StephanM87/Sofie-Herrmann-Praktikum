
Bouldern = {
                "name":"Bouldern",
                "Kosten":"10€"
            }

Kochen = {
                "name":"Kochen",
                "Kosten":"15€"
            }
Vogelkunde = {
                "name":"Vogelkunde",
                "Kosten":"15€"
            }
Sofie={"name":"Sofie",
            "lastName":"Herrmann",
            "Hobbies":[Bouldern,Kochen ]}

Dieter={
        "name":"Dieter",
        "lastName":"Herrmann",
        "Hobbies":[Bouldern,Vogelkunde]}



def kostenAusgabe(dict):
    print(dict["name"], dict["Kosten"])



def hobbyExtractor(dict):
    print("Runde")
    hobby = dict["Hobbies"]
    for i in hobby:
        kostenAusgabe(i)



family_dict = {"individuum":[Sofie,Dieter]}
individuals = family_dict["individuum"]

for i in individuals:
    hobbyExtractor(i)










