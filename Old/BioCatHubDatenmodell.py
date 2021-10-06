
DataModel = {
    "title": "EcPDC_C-HispH6.5",
    "description": "Reaction under argon atmosphere",
    "enzymes": [
        {
            "concentration": "1",
            "ecNumber": "4.1.1.1",
            "formulation": "NiNTA pruified enzyme",
            "method": "Bradford",
            "name": "pyruvate decarboxylase",
            "organism": "E.coli",
            "others": [

            ],
            "reaction": {
                "educts": [
                    {
                        "concentration": "1",
                        "formula": "C3H4O3",
                        "id": "33",
                        "imageUrl": "https://www.ebi.ac.uk/chebi/displayImage.do?defaultImage=true&imageIndex=0&chebiId=32816",
                        "name": "Pyruvate",
                        "purity": "98%",
                        "role": "substrate",
                        "smiles": "CC(=O)C(O)=O",
                        "supplier": "sigma-aldrich",
                        "unit": "mmoL/L"
                    }
                ],
                "products": [
                    {
                        "concentration": "1",
                        "formula": "C2H4O",
                        "id": "1292",
                        "imageUrl": "https://www.ebi.ac.uk/chebi/displayImage.do?defaultImage=true&imageIndex=0&chebiId=15343",
                        "name": "Acetaldehyde",
                        "purity": "0",
                        "role": "product",
                        "smiles": "CC=O",
                        "supplier": "0",
                        "unit": "mmoL/L"
                    },
                    {
                        "concentration": "0.5",
                        "formula": "CO2",
                        "id": "1266",
                        "imageUrl": "https://www.ebi.ac.uk/chebi/displayImage.do?defaultImage=true&imageIndex=0&chebiId=139538",
                        "name": "CO2",
                        "purity": "0",
                        "role": "product",
                        "smiles": "O=C=O",
                        "supplier": "0",
                        "unit": "mmoL/L"
                    }
                ],
                "value": "Pyruvate = Acetaldehyde + CO2"
            },
            "sequence": "maatttatsl fssrlhfqnq \nnqgygfpakt pnslqvnqii \ndgrkmrnatv lsaastdkai\nttaqsvapta cdrvrrhtis \nvfvgdesgii nriagvfarr \ngynieslavg lnedkalfti\nvvlgtdkvlq qvveqlnklv \nnvikvedlsk ephverelml \niklnadpstr seimwlvdif\nrakivdtseq sltievtgdp \ngkmvalttnl ekfgikeiar \ntgkialrrek mgetapfwrf\nsaasyphlvk esshetvaek \ntklaltgngn assggdvypv \nepyndfkpvl dahwgmvyde\ndssglrshtl sllvanvpgv \nlnlitgaisr rgyniqslav \ngpaekeglsr ittvipgtde\nnidklvrqlq klidlqeiqn \nithmpfaere lmlikvaadt \nsarrdvldia qvfrakaidv\nsdhtitlevt gdlrkmsalq \ntqleaygice vartgrvalv \nresgvdstyl rgyslpl\n",
            "type": "variant",
            "unit": "mg/mL",
            "variant": "EcPDC_C-His"
        }
    ],
    "vessel": {
        "others": [

        ],
        "type": "microcentrifuge tube 1.5 mL polypropylene",
        "unit": "mL",
        "volume": "1"
    },
    "condition": {
        "buffer": {
            "concentration": "100",
            "type": "Kpi-buffer",
            "unit": "mmoL/L"
        },
        "others": [
            {
                "key": "gas phase",
                "value": "argon"
            }
        ],
        "ph": "6.5",
        "temp": "30",
        "unit": "\u00b0C"
    },
    "experimentalData": {
        "measurements": [
            {
                "notes": "absorption measurement at 333 nm",
                "plotStyle": "point",
                "reagent": "Pyruvate",
                "replicates": [
                    {
                        "x_value": 0,
                        "y_values": [
                            0.04270564516129032,
                            0.04101612903225807,
                            0.03994758064516129
                        ]
                    },
                    {
                        "x_value": 5,
                        "y_values": [
                            0.04270564516129032,
                            0.04101612903225807,
                            0.03961693548387097
                        ]
                    },
                    {
                        "x_value": 10,
                        "y_values": [
                            0.04199193548387097,
                            0.040491935483870964,
                            0.03964516129032258
                        ]
                    },
                    {
                        "x_value": 15,
                        "y_values": [
                            0.042153225806451616,
                            0.04061693548387097,
                            0.039495967741935485
                        ]
                    },
                    {
                        "x_value": 20,
                        "y_values": [
                            0.04196774193548387,
                            0.04068548387096774,
                            0.03968145161290322
                        ]
                    },
                    {
                        "x_value": 25,
                        "y_values": [
                            0.04191935483870968,
                            0.04043951612903225,
                            0.039294354838709675
                        ]
                    },
                    {
                        "x_value": 30,
                        "y_values": [
                            0.041399193548387093,
                            0.040270161290322584,
                            0.039455645161290326
                        ]
                    },
                    {
                        "x_value": 35,
                        "y_values": [
                            0.041177419354838714,
                            0.03980645161290322,
                            0.039294354838709675
                        ]
                    },
                    {
                        "x_value": 40,
                        "y_values": [
                            0.04135483870967742,
                            0.039786290322580645,
                            0.0389758064516129
                        ]
                    },
                    {
                        "x_value": 45,
                        "y_values": [
                            0.04135483870967742,
                            0.03961693548387097,
                            0.03881048387096774
                        ]
                    },
                    {
                        "x_value": 50,
                        "y_values": [
                            0.04061693548387097,
                            0.039495967741935485,
                            0.03865725806451613
                        ]
                    },
                    {
                        "x_value": 55,
                        "y_values": [
                            0.04101612903225807,
                            0.039294354838709675,
                            0.03852016129032258
                        ]
                    },
                    {
                        "x_value": 60,
                        "y_values": [
                            0.040491935483870964,
                            0.03913306451612903,
                            0.038221774193548386
                        ]
                    },
                    {
                        "x_value": 65,
                        "y_values": [
                            0.040318548387096774,
                            0.03881048387096774,
                            0.03802822580645161
                        ]
                    },
                    {
                        "x_value": 70,
                        "y_values": [
                            0.04035887096774193,
                            0.03865725806451613,
                            0.037754032258064514
                        ]
                    },
                    {
                        "x_value": 75,
                        "y_values": [
                            0.03994758064516129,
                            0.03869758064516129,
                            0.037423387096774195
                        ]
                    },
                    {
                        "x_value": 80,
                        "y_values": [
                            0.039786290322580645,
                            0.03833467741935484,
                            0.03760887096774193
                        ]
                    },
                    {
                        "x_value": 85,
                        "y_values": [
                            0.03961693548387097,
                            0.038120967741935484,
                            0.037125
                        ]
                    },
                    {
                        "x_value": 90,
                        "y_values": [
                            0.03923387096774193,
                            0.037625,
                            0.037088709677419354
                        ]
                    },
                    {
                        "x_value": 95,
                        "y_values": [
                            0.03911693548387096,
                            0.037625,
                            0.03688306451612903
                        ]
                    },
                    {
                        "x_value": 100,
                        "y_values": [
                            0.03895564516129032,
                            0.0374758064516129,
                            0.036625
                        ]
                    },
                    {
                        "x_value": 105,
                        "y_values": [
                            0.03864112903225807,
                            0.037213709677419354,
                            0.03657258064516129
                        ]
                    },
                    {
                        "x_value": 110,
                        "y_values": [
                            0.038177419354838704,
                            0.03689516129032258,
                            0.0361008064516129
                        ]
                    },
                    {
                        "x_value": 115,
                        "y_values": [
                            0.038221774193548386,
                            0.036762096774193544,
                            0.03591129032258064
                        ]
                    },
                    {
                        "x_value": 120,
                        "y_values": [
                            0.0379758064516129,
                            0.036762096774193544,
                            0.03566129032258064
                        ]
                    },
                    {
                        "x_value": 125,
                        "y_values": [
                            0.03757258064516129,
                            0.03633064516129032,
                            0.035399193548387095
                        ]
                    },
                    {
                        "x_value": 130,
                        "y_values": [
                            0.037375,
                            0.035798387096774194,
                            0.03544354838709678
                        ]
                    },
                    {
                        "x_value": 135,
                        "y_values": [
                            0.037125,
                            0.03566935483870968,
                            0.03502016129032258
                        ]
                    },
                    {
                        "x_value": 140,
                        "y_values": [
                            0.03688306451612903,
                            0.035556451612903224,
                            0.03492338709677419
                        ]
                    },
                    {
                        "x_value": 145,
                        "y_values": [
                            0.03674596774193548,
                            0.03530241935483871,
                            0.03450806451612903
                        ]
                    },
                    {
                        "x_value": 150,
                        "y_values": [
                            0.03633064516129032,
                            0.03497177419354838,
                            0.03427016129032258
                        ]
                    },
                    {
                        "x_value": 155,
                        "y_values": [
                            0.036016129032258065,
                            0.03492338709677419,
                            0.03416532258064516
                        ]
                    },
                    {
                        "x_value": 160,
                        "y_values": [
                            0.035883064516129035,
                            0.03456048387096774,
                            0.03387903225806451
                        ]
                    },
                    {
                        "x_value": 165,
                        "y_values": [
                            0.035491935483870966,
                            0.03429838709677419,
                            0.033342741935483866
                        ]
                    },
                    {
                        "x_value": 170,
                        "y_values": [
                            0.03538709677419355,
                            0.03401209677419355,
                            0.033068548387096774
                        ]
                    },
                    {
                        "x_value": 175,
                        "y_values": [
                            0.03522983870967742,
                            0.033483870967741934,
                            0.032943548387096774
                        ]
                    },
                    {
                        "x_value": 180,
                        "y_values": [
                            0.03497177419354838,
                            0.03338306451612903,
                            0.03264919354838709
                        ]
                    },
                    {
                        "x_value": 185,
                        "y_values": [
                            0.03437096774193549,
                            0.033068548387096774,
                            0.03252419354838709
                        ]
                    },
                    {
                        "x_value": 190,
                        "y_values": [
                            0.03427016129032258,
                            0.03270967741935484,
                            0.03204838709677419
                        ]
                    },
                    {
                        "x_value": 195,
                        "y_values": [
                            0.03361290322580645,
                            0.03263306451612903,
                            0.03189112903225807
                        ]
                    },
                    {
                        "x_value": 200,
                        "y_values": [
                            0.03364516129032258,
                            0.0322258064516129,
                            0.03175806451612903
                        ]
                    },
                    {
                        "x_value": 205,
                        "y_values": [
                            0.03318145161290322,
                            0.0318991935483871,
                            0.031427419354838705
                        ]
                    },
                    {
                        "x_value": 210,
                        "y_values": [
                            0.03318145161290322,
                            0.03168951612903226,
                            0.03087096774193548
                        ]
                    },
                    {
                        "x_value": 215,
                        "y_values": [
                            0.03260483870967742,
                            0.031338709677419356,
                            0.03073790322580645
                        ]
                    },
                    {
                        "x_value": 220,
                        "y_values": [
                            0.03234274193548387,
                            0.030979838709677417,
                            0.030181451612903226
                        ]
                    },
                    {
                        "x_value": 225,
                        "y_values": [
                            0.03194354838709677,
                            0.030669354838709677,
                            0.030016129032258063
                        ]
                    },
                    {
                        "x_value": 230,
                        "y_values": [
                            0.03178225806451613,
                            0.030443548387096772,
                            0.029778225806451612
                        ]
                    },
                    {
                        "x_value": 235,
                        "y_values": [
                            0.031262096774193546,
                            0.030181451612903226,
                            0.02942338709677419
                        ]
                    },
                    {
                        "x_value": 240,
                        "y_values": [
                            0.031108870967741932,
                            0.029754032258064514,
                            0.02920967741935484
                        ]
                    },
                    {
                        "x_value": 245,
                        "y_values": [
                            0.030669354838709677,
                            0.02956854838709677,
                            0.028741935483870967
                        ]
                    },
                    {
                        "x_value": 250,
                        "y_values": [
                            0.030411290322580643,
                            0.029040322580645157,
                            0.028459677419354838
                        ]
                    },
                    {
                        "x_value": 255,
                        "y_values": [
                            0.03007258064516129,
                            0.028754032258064513,
                            0.028129032258064516
                        ]
                    },
                    {
                        "x_value": 260,
                        "y_values": [
                            0.02979032258064516,
                            0.028495967741935482,
                            0.02781048387096774
                        ]
                    },
                    {
                        "x_value": 265,
                        "y_values": [
                            0.02921774193548387,
                            0.028326612903225808,
                            0.02752016129032258
                        ]
                    },
                    {
                        "x_value": 270,
                        "y_values": [
                            0.028999999999999998,
                            0.027983870967741933,
                            0.027213709677419356
                        ]
                    },
                    {
                        "x_value": 275,
                        "y_values": [
                            0.028725806451612903,
                            0.02746774193548387,
                            0.026806451612903223
                        ]
                    },
                    {
                        "x_value": 280,
                        "y_values": [
                            0.0282741935483871,
                            0.02715725806451613,
                            0.026588709677419352
                        ]
                    },
                    {
                        "x_value": 285,
                        "y_values": [
                            0.02829838709677419,
                            0.02697983870967742,
                            0.026302419354838708
                        ]
                    },
                    {
                        "x_value": 290,
                        "y_values": [
                            0.02766935483870968,
                            0.02649193548387097,
                            0.025891129032258063
                        ]
                    },
                    {
                        "x_value": 295,
                        "y_values": [
                            0.027407258064516125,
                            0.0262258064516129,
                            0.025673387096774195
                        ]
                    },
                    {
                        "x_value": 300,
                        "y_values": [
                            0.02711290322580645,
                            0.025911290322580643,
                            0.025419354838709676
                        ]
                    }
                ],
                "x_name": "time",
                "x_unit": "s",
                "y_name": "concentration",
                "y_unit": "mol/l"
            }
        ]
    },
    "user": {
        "email": "s.malzacher@fz-juelich.de",
        "firstName": "Stephan",
        "institution": "Forschungszentrum J\u00fclich",
        "lastName": "Malzacher"
    }
}
