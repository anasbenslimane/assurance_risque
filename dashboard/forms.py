from django import forms

VEH_BRANDS = [
    ("B1", "B1"),
    ("B2", "B2"),
    ("B3", "B3"),
    ("B4", "B4"),
    ("B5", "B5"),
    ("B6", "B6"),
    ("B10", "B10"),
    ("B11", "B11"),
    ("B12", "B12"),
    ("B13", "B13"),
    ("B14", "B14"),
]

VEH_GAS = [
    ("Diesel", "Diesel"),
    ("Regular", "Regular"),
]

AREAS = [
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
]

REGIONS = [
    ("Aquitaine", "Aquitaine"),
    ("Basse-Normandie", "Basse-Normandie"),
    ("Bretagne", "Bretagne"),
    ("Centre", "Centre"),
    ("Haute-Normandie", "Haute-Normandie"),
    ("Ile-de-France", "Ile-de-France"),
    ("Limousin", "Limousin"),
    ("Nord-Pas-de-Calais", "Nord-Pas-de-Calais"),
    ("Pays-de-la-Loire", "Pays-de-la-Loire"),
    ("Picardie", "Picardie"),
    ("Poitou-Charentes", "Poitou-Charentes"),
    ("Rhone-Alpes", "Rhone-Alpes"),
]

class PredictionForm(forms.Form):

    Exposure = forms.TypedChoiceField(
    label="Durée d'exposition",
    choices=[
        (0, "0 mois"),
        (0.25, "3 mois"),
        (0.5, "6 mois"),
        (0.75, "9 mois"),
        (1, "12 mois (1 an)"),
    ],
    coerce=float,
    widget=forms.Select(attrs={
        "class": "form-select"
    })
)

    VehPower = forms.TypedChoiceField(
    label="Puissance du véhicule",
    choices=[
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
        (11, "11"),
        (12, "12"),
        (13, "13"),
        (14, "14"),
        (15, "15"),
    ],
    coerce=int,
    widget=forms.Select(attrs={
        "class": "form-select"
    })
)

    VehAge = forms.IntegerField(
        min_value=0,
        label="Âge du véhicule"
    )

    DrivAge = forms.IntegerField(
        min_value=18,
        label="Âge du conducteur"
    )

    BonusMalus = forms.IntegerField(
        min_value=50,
        label="Bonus-Malus"
    )

    VehBrand = forms.ChoiceField(
        choices=VEH_BRANDS,
        label="Marque du véhicule"
    )

    VehGas = forms.ChoiceField(
        choices=VEH_GAS,
        label="Carburant"
    )

    Area = forms.ChoiceField(
        choices=AREAS,
        label="Zone"
    )

    Density = forms.IntegerField(
        min_value=0,
        label="Densité"
    )

    Region = forms.ChoiceField(
        choices=REGIONS,
        label="Région"
    )